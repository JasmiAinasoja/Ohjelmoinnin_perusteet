import hashlib
import os

CREDENTIALS_FILE = "credentials.txt"


def hash_password(password: str) -> str:
    """Hash the password using MD5 and return hex digest."""
    return hashlib.md5(password.encode()).hexdigest()


def load_credentials():
    """Load credentials from file into a list of tuples (id, username, hashed_password)."""
    if not os.path.exists(CREDENTIALS_FILE):
        return []
    with open(CREDENTIALS_FILE, "r") as file:
        lines = file.readlines()
    credentials = []
    for line in lines:
        parts = line.strip().split(";")
        if len(parts) == 3:
            credentials.append((int(parts[0]), parts[1], parts[2]))
    return credentials

def save_credentials(credentials):
    """Save credentials list back to file."""
    with open(CREDENTIALS_FILE, "w") as file:
        for cred in credentials:
            file.write(f"{cred[0]};{cred[1]};{cred[2]}\n")

def register_user():
    username = input("Insert username: ")
    password = input("Insert password: ")
    credentials = load_credentials()
    user_id = len(credentials)
    hashed_password = hash_password(password)
    credentials.append((user_id, username, hashed_password))
    save_credentials(credentials)
    print("User registration completed!")

def login_user():
    username = input("Insert username: ")
    password = input("Insert password: ")
    hashed_password = hash_password(password)
    credentials = load_credentials()
    for user_id, user_name, stored_hash in credentials:
        if user_name == username and stored_hash == hashed_password:
            print("Authentication successful!")
            user_menu(user_id, username)
            return
    print("Authentication failed!")


def user_menu(user_id, username):
    while True:
        print("\nUser menu:")
        print("1 - View profile")
        print("2 - Change password")
        print("0 - Logout")
        choice = input("Your choice: ")
        if choice == "1":
            print(f"Profile ID {user_id} - {username}")
        elif choice == "2":
            print("Change password feature not implemented.")
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")


def main():
    print("Program starting.")
    while True:
        print("\nOptions:")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            login_user()
        elif choice == "2":
            register_user()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
    print("\nProgram ending.")


if __name__ == "__main__":
    main()
