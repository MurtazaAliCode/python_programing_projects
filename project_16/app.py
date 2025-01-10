
Name = "Admin"
Password = "Admin123"

def login():
    print("\n--- Login Page ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    if username in Name and password == Password:
        print(f"\nWelcome, {username}! You have successfully logged in.\n")
    else:
        print("\nInvalid username or password. Please try again.\n")


 


