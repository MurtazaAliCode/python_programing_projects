# Contact Management Book

contacts = {}

while True:
    print("\nContact Management Book\n")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ").strip()
        if name in contacts:
            print(f"Contact name {name} already exists.")
        else:
            age = input("Enter your age: ").strip()
            mobile = input("Enter your mobile number: ").strip()
            contacts[name] = {"Age": int(age), "Mobile": mobile}
            print(f"Contact {name} has been created successfully.")

    elif choice == "2":
        name = input("Enter the name to view: ").strip()
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {contact['Age']}, Mobile number: {contact['Mobile']}")
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter the name to update: ").strip()
        if name in contacts:
            new_name = input("Enter updated name: ").strip()
            age = input("Enter updated age: ").strip()
            mobile = input("Enter updated mobile number: ").strip()
            contacts.pop(name)  # Remove the old contact
            contacts[new_name] = {"Age": int(age), "Mobile": mobile}
            print(f"Contact {new_name} has been updated successfully.")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter the name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print("Contact not found!")

    elif choice == "5":
        search_name = input("Enter contact name to search: ").strip()
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Name: {name}, Age: {contact['Age']}, Mobile number: {contact['Mobile']}")
                found = True
        if not found:
            print("Contact not found!")

    elif choice == "6":
        print(f"Total contacts in your contact book: {len(contacts)}")

    elif choice == "7":
        print("Goodbye... Closing the program.")
        break

    else:
        print("Invalid input. Please try again.")
