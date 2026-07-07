# contact_book.py
# Project: Simple Contact Book (using dictionary + file)

import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=2)

contacts = load_contacts()

print("=== Contact Book ===\n")

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    
    choice = input("\nEnter choice: ")
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        save_contacts(contacts)
        print("Contact saved!")
        
    elif choice == "2":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
            
    elif choice == "3":
        search = input("Search name: ")
        if search in contacts:
            print(f"{search}: {contacts[search]}")
        else:
            print("Contact not found.")
            
    elif choice == "4":
        print("Goodbye!")
        break
