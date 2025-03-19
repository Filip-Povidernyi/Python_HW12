from handler import handlers


def main():

    print("Welcome to the assistant bot!")

    book = handlers['load']()

    while True:

        command = input("Enter a command: ").strip().lower()
        cmd, args = handlers['command_parser'](command)

        match cmd:

            case "hello":
                print("How can I help you?")

            case "add":
                print(handlers['add_contact'](args, book))

            case "change":
                print(handlers['change_contact'](args, book))

            case "phone":
                print(handlers['show_phone'](args, book))

            case "del-phone":
                print(handlers['del_phone'](args, book))

            case "all":
                handlers['show_all'](book)

            case "add-birthday":
                print(handlers['add_birthday'](args, book))

            case "show-birthday":
                print(handlers['show_birthday'](args, book))

            case "birthdays":
                if isinstance(handlers['birthdays'](book), list):
                    print(f"Список привітань на цьому тижні:\n" +
                          "\n".join(str(birthday) for birthday in handlers['birthdays'](book)))
                else:
                    print(handlers['birthdays'](book))

            case "exit":
                print(handlers['save_book'](book))
                break

            case "close":
                print(handlers['save_book'](book))
                break

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
