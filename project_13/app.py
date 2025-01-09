import os

def create_file(file_name):
    try:
        with open("file_name", "x") as f:
            print(f"{file_name} created successfully.")

    except FileExistsError:
        print(f"File {file_name} already exists.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found.")

    else:
        print("Files in the directory:")
        for file in files:
            print(file)

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"{file_name} deleted successfully.")

    except FileNotFoundError:
        print(f"File {file_name} not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(file_name):
    try:
        with open("file_name", "r") as f:
            content = f.read()
            print(f"Content of {file_name}:\n{content}")

    except FileNotFoundError:
        print(f"File {file_name} not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(file_name):
    try:
        with open("file_name", "a") as f:
            content = input("Enter data to add: ")
            f.write(content + "\n")
            print(f"Content added to {file_name} successfully.")

    except FileNotFoundError:
        print(f"File {file_name} not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

def display_menu():
    while True:
        print("\nFile management app:")
        print("1: Create file")
        print("2: View all files")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit")

        choice = input("Enter a number to perform a task (1-6): ")

        if choice == "1":
            file_name = input("Enter the file name to create: ")
            create_file(file_name)

        elif choice == "2":
            view_all_files()

        elif choice == "3":
            file_name = input("Enter the file name to delete: ")
            delete_file(file_name)

        elif choice == "4":
            file_name = input("Enter the file name to read: ")
            read_file(file_name)

        elif choice == "5":
            file_name = input("Enter the file name to edit: ")
            edit_file(file_name)

        elif choice == "6":
            print("Exiting the application...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the program
display_menu()
