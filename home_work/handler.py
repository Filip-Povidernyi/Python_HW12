from functools import wraps
from pathlib import Path
import pickle
from record import Record

from address_book import AddressBook


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except ValueError as error:
            if func.__name__ == 'add_contact':
                return 'For add contact, please, enter <add name phone>. Phone number containe 10 digits!'
            elif func.__name__ == 'change_contact':
                return 'For change contact, please, enter <change name old_phone new_phone>'
            elif func.__name__ == 'add_birthday':
                return str(error)
            elif func.__name__ == "show_birthday":
                return str(error)
            elif func.__name__ == 'del_phone':
                return 'For remove phone number, please, enter <del-phone name phone>'

        except IndexError as error:
            if func.__name__ == 'show_phone':
                return 'For get phone number, please, enter <phone name>'
            elif func.__name__ == 'del_phone':
                return str(error)

        except KeyError as error:
            if func.__name__ == 'add_contact':
                return str(error)
            elif func.__name__ == 'change_contact':
                return str(error)
            elif func.__name__ == 'show_phone':
                return str(error)
            elif func.__name__ == 'add_birthday':
                return str(error)
            elif func.__name__ == 'show_birthday':
                return str(error)

    return inner


def command_parser(command: str):

    cmd, *args = command.split(' ')
    cmd = cmd.strip().lower()

    return cmd, args


@input_error
def add_contact(args: list, book: AddressBook):

    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    if phone:
        record.add_phone(phone)

    return message


@input_error
def change_contact(args: list, book: AddressBook):

    name, old_phone, new_phone = args
    record = book.find(name)

    if record is None:
        raise KeyError(f'This name: {name.title()} is absent')

    return record.edit_phone(old_phone, new_phone)


@input_error
def show_phone(args: list, book: AddressBook):

    name = args[0]

    if name in book.data.keys():
        return book.data[name]

    else:
        raise KeyError(f'No contact with name {name.title()}.')


@input_error
def del_phone(args: list, book: AddressBook):

    name, phone = args
    record = book.find(name)

    if phone in [p.value for p in record.phones]:

        record.remove_phone(phone)
        return f"Phone {phone} removed!"

    else:
        raise IndexError("Number is ubsent in contact")


def show_all(book: AddressBook):

    if not book.data:
        return "No contacts in your phonebook"
    else:
        for record in book.data.values():
            print(f"{record}")


@input_error
def add_birthday(args: list, book: AddressBook):

    name, birth_date = args
    record = book.find(name)

    if record:
        return record.add_birthday(birth_date)

    if record is None:
        raise KeyError(f'No contact with name {name.title()}.')


@input_error
def show_birthday(args: list, book: AddressBook):

    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError(f'No contact with name {name.title()}.')

    if record.birthday is not None:
        return f"{name.title()}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
    else:
        raise ValueError(f"{name.title()}'s birthday not added")


def birthdays(book: AddressBook):

    return book.get_congrats()


def load():

    path = Path('contacts.pkl')

    if path.exists() and path.is_file():

        with open('contacts.pkl', 'rb') as file:
            return pickle.load(file)
    else:
        return AddressBook()


def save_book(book: AddressBook):

    with open('contacts.pkl', 'wb') as file:
        pickle.dump(book, file)
        return "Good bye!"


handlers = {
    'add_contact': add_contact,
    'change_contact': change_contact,
    'show_phone': show_phone,
    'del_phone': del_phone,
    'show_all': show_all,
    'add_birthday': add_birthday,
    'show_birthday': show_birthday,
    'birthdays': birthdays,
    'load': load,
    'save_book': save_book,
    'command_parser': command_parser
}
