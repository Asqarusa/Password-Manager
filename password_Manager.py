import hashlib
import getpass

password_manager = {}

def creat_account():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account Created Successfully! ")



def login():
    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login Successfully!")
    else:
        print("Invalid Login and Password?!")


def main():
    while True:
        choice = input("Enter 1 to Creat Account, Enter 2 to Log in, or Enter 0 to Exit: ")
        if choice == "1":
            creat_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print(" invalid input!")

if __name__ == "__main__":
    main()












