import json
import os

CONTACT_FILE = 'contacts.json'


def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    store_name = input("Enter Store Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts.append({
        "store_name": store_name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts(contacts)
    print("Contact added successfully!\n")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nAll Contacts:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['store_name']} - {c['phone']}")
    print()


def search_contact(contacts):
    query = input("Enter name or phone to search: ").lower()
    found = [c for c in contacts if query in c['store_name'].lower() or query in c['phone']]

    if not found:
        print("No matching contact found.\n")
    else:
        print("\nSearch Results:")
        for c in found:
            print_contact(c)


def print_contact(contact):
    print(f"Store Name: {contact['store_name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}\n")


def update_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to update: ")) - 1

    if 0 <= index < len(contacts):
        contact = contacts[index]
        print("Leave blank to keep current value.\n")
        contact['store_name'] = input(f"Store Name [{contact['store_name']}]: ") or contact['store_name']
        contact['phone'] = input(f"Phone [{contact['phone']}]: ") or contact['phone']
        contact['email'] = input(f"Email [{contact['email']}]: ") or contact['email']
        contact['address'] = input(f"Address [{contact['address']}]: ") or contact['address']
        save_contacts(contacts)
        print("Contact updated successfully!\n")
    else:
        print("Invalid contact number.\n")


def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to delete: ")) - 1

    if 0 <= index < len(contacts):
        deleted = contacts.pop(index)
        save_contacts(contacts)
        print(f"Deleted contact: {deleted['store_name']}\n")
    else:
        print("Invalid contact number.\n")


def main():
    contacts = load_contacts()
    while True:
        print("===== Contact Management =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.\n")


if __name__ == "__main__":
    main()
