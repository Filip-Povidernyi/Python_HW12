from handler import command_parser, add_contact, show_phone, show_all, change_contact, add_birthday, show_birthday, birthdays, del_phone, load, save_book


def main():

    print("Welcome to the assistant bot!")

    book = load()

    while True:

        command = input("Enter a command: ").strip().lower()
        cmd, args = command_parser(command)

        match cmd:

            case "hello":
                print("How can I help you?")

            case "add":
                print(add_contact(args, book))

            case "change":
                print(change_contact(args, book))

            case "phone":
                print(show_phone(args, book))

            case "del-phone":
                print(del_phone(args, book))

            case "all":
                show_all(book)

            case "add-birthday":
                print(add_birthday(args, book))

            case "show-birthday":
                print(show_birthday(args, book))

            case "birthdays":
                if isinstance(birthdays(book), list):
                    print(f"Список привітань на цьому тижні:\n" +
                          "\n".join(str(birthday) for birthday in birthdays(book)))
                else:
                    print(birthdays(book))

            case "exit":
                print(save_book(book))
                break

            case "close":
                print(save_book(book))
                break

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
