contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("CONTACT ADDED SUCCESSFULLY")


def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n---- CONTACT LIST ----")
    for i, contact in enumerate(contacts, start=1):
        #print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")
        print(f"\nContact {i}")
        print(f"Name    : {contact['name']}")
        print(f"Phone   : {contact['phone']}")
        print(f"Email   : {contact['email']}")
        print(f"Address : {contact['address']}")

def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False

    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            print("\nContact found:")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    view_contacts()
    try:
        choice = int(input("Enter contact number to update: ")) - 1

        if 0 <= choice < len(contacts):
            contact = contacts[choice]
            print("Leave blank to keep old value")

            name = input(f"New name ({contact['name']}): ") or contact['name']
            phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
            email = input(f"New email ({contact['email']}): ") or contact['email']
            address = input(f"New address ({contact['address']}): ") or contact['address']

            contact.update({
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            })

            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_contact():
    view_contacts()
    try:
        choice = int(input("Enter contact number to delete: ")) - 1

        if 0 <= choice < len(contacts):
            contacts.pop(choice)
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


def menu():
    while True:
        print("\n--- CONTACT BOOK MENU ---")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


menu()
