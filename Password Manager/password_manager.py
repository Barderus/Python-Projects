import os
import json
import hashlib
import getpass
import random
import string
from cryptography.fernet import Fernet

'''
json is a library for encoding and decoding JSON (JavaScript Object Notation) data, 
    commonly used for data serialization and interchange.

hashlib is a library that provides secure hash functions, including SHA-256, for creating hash values from data, 
    often used for password hashing and data integrity verification. You can check this tutorial on how to use it.

getpass: A library for safely and interactively entering sensitive information like passwords without displaying the 
    input on the screen. Similar to the way the Linux terminals are.

os: A library for interacting with the operating system, allowing you to perform tasks like file 
    and directory manipulation.

sys: This module is a built-in Python module that provides access to various system-specific parameters and functions.

cryptography.fernet: Part of the cryptography library, it provides the Fernet symmetric-key encryption method for 
    securely encrypting and decrypting data.
    
Login credentials will be stored in the user_data.json file.

Passwords will be stored in the passwords.json file.
'''


class PasswordManager:
    def __init__(self, key_filename='encryption_key.key'):
        self.key_filename = key_filename
        self.cipher = self.initialize_cipher()

    def generate_key(self):
        return Fernet.generate_key()

    def load_or_generate_key(self):
        if os.path.exists(self.key_filename):
            with open(self.key_filename, 'rb') as key_file:
                return key_file.read()
        else:
            key = self.generate_key()
            with open(self.key_filename, 'wb') as key_file:
                key_file.write(key)
            return key

    def initialize_cipher(self):
        key = self.load_or_generate_key()
        return Fernet(key)

    def hash_password(self, password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode())
        return sha256.hexdigest()

    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        return self.cipher.decrypt(encrypted_password.encode()).decode()

    def check_duplicates(self, file_name, username, password):
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    users = []
        else:
            users = []

        for user in users:
            if user["username"] == username and self.decrypt_password(user["master_password"]) == password:
                print("Username or password has already been used.")
                return True
        return False

    def register(self):
        file_name = "user_data.json"
        username = input("Enter your username: ")
        master_password = getpass.getpass("Enter your master password: ")

        if self.check_duplicates(file_name, username, master_password):
            return

        hashed_master_password = self.hash_password(master_password)

        user_data = {"username": username, "master_password": hashed_master_password}

        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    users = []
        else:
            users = []

        users.append(user_data)

        with open(file_name, "w") as file:
            json.dump(users, file, indent=4)
            print("Account created with success. Returning to the main menu.")
            self.main_menu()

    def login(self, username, password):
        file_name = "user_data.json"

        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    users = []
        else:
            users = []

        hashed_password = self.hash_password(password)

        for user in users:
            if user["username"] == username and user["master_password"] == hashed_password:
                print("Login successful.")
                self.menu()
                return
        print("Invalid credentials. Try again or create an account if you have not done it yet.")

    def new_password(self):
        info = []
        title = input("Enter the type ( Login/ Identity/ Note/ Card): ")
        login = input("Enter your username: ")
        password = getpass.getpass(prompt="Enter your password: ")
        confirm_password = getpass.getpass(prompt="Confirm your password: ")

        while True:
            if password != confirm_password:
                print("\n\tPasswords do not match.")
                confirm_password = getpass.getpass(prompt="Confirm your password: ")
            else:
                break

        info_data = {"title": title, "login": login, "password": password}
        info.append(info_data)

        with open("password.json", "w") as file:
            json.dump(info_data, file)
            print("\nInformation registered with success. Returning to the main menu.")
            self.menu()

    def read_words(self, filename):
        with open(filename, "r") as file:
            words = file.readlines
            return words
    def gen_password(self):
        choice = input("""Choose the type of password you would like to generate: 
                    1. Password
                    2. Passphrase
                    3. Exit
                    """)
        if choice == 1:
            length = int(input("Enter the desired length of your password: "))
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            print(f"Your password is {password}")
        elif choice == 2:
            words = int(input("Enter how many words you would like to have: "))
            separator = input("Enter the words separator character: ")
        else:
            exit()

    def view_passwords(self):
        pass

    def menu(self):
        choice = int(input("""
            1. Enter new password
            2. Generate new password
            3. View passwords
            4. Exit
        """))

        if choice == 1:
            self.new_password()
        elif choice == 2:
            self.gen_password()
        elif choice == 3:
            self.view_passwords()
        else:
            exit()

    def main_menu(self):
        while True:
            choice = int(input("""
                1. Create a new account
                2. Access account
                3. Exit
            """))

            if choice == 1:
                self.register()
            elif choice == 2:
                username = input("Username: ")
                password = getpass.getpass(prompt="Password: ")
                self.login(username, password)
            else:
                exit()

    def words(self):
        sub_nouns = self.read_words("sub_nouns.txt")
        adjectives = self.read_words("adjectives_list.txt")
        nouns = self.read_words("nouns_list.txt")
        verbs = self.read_words("verbs_list.txt")
        obj_nouns = self.read_words("obj_nouns.txt")


def main():
    manager = PasswordManager()
    manager.main_menu()


if __name__ == "__main__":
    main()
