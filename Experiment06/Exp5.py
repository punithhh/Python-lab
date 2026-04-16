phonebook = {}

while True:
    print("\n===== PHONEBOOK MENU =====")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Display All Contacts")
    print("6. Display All Names (Keys)")
    print("7. Display All Numbers (Values)")
    print("8. Display All Entries (Items)")
    print("9. Count Contacts")
    print("10. Copy Phonebook")
    print("11. Clear Phonebook")
    print("12. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print("Contact added successfully.")

        case 2:
            name = input("Enter name to update: ")
            if name in phonebook:
                number = input("Enter new number: ")
                phonebook.update({name: number})
                print("Contact updated.")
            else:
                print("Contact not found.")

        case 3:
            name = input("Enter name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print("Contact deleted.")
            else:
                print("Contact not found.")

        case 4:
            name = input("Enter name to search: ")
            if name in phonebook:
                print("Phone number:", phonebook.get(name))
            else:
                print("Contact not found.")

        case 5:
            if phonebook:
                print("\nAll Contacts:")
                for name, number in phonebook.items():
                    print(name, ":", number)
            else:
                print("Phonebook is empty.")

        case 6:
            print("Names:", list(phonebook.keys()))

        case 7:
            print("Numbers:", list(phonebook.values()))

        case 8:
            print("Entries:", list(phonebook.items()))

        case 9:
            print("Total contacts:", len(phonebook))

        case 10:
            copy_phonebook = phonebook.copy()
            print("Copied Phonebook:", copy_phonebook)

        case 11:
            phonebook.clear()
            print("Phonebook cleared.")

        case 12:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice. Try again.")
