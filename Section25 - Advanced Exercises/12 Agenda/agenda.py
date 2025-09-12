import time


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                found_contact = contact
                return found_contact
    
    def show_contacts(self):
        for contact in self.contacts:
            print (contact)

def menu():
    agenda = Agenda()
    while True:
        print("--- Menu ---")
        print("1. Add contact")
        print("2. Search contacts")
        print("3. Show all contacts")
        print("4. Exit")
        
        answer = input("Select an option (1-4): ")
        if answer == "1":
            name_insert = input("Name: ")
            phone_insert = input("Phone: ")
            email_insert = input("Email: ")
            contact1 = Contact(name_insert, phone_insert, email_insert)

            agenda.add_contact(contact1)
            print(f"✅ Contact {contact1.name} succesfully added.")
            time.sleep(2)

        elif answer == "2":
            searched_name = input("Name of the contact to search: ")
            contact_found = agenda.search_contact(searched_name)
            if contact_found:
                print(f"🔍 Contact found:\nName: {contact_found.name}, Phone: {contact_found.phone}, Email: {contact_found.email}")
                time.sleep(2)
            else:
                print ("Contact not found")
        
        elif answer == "3":
                contact = agenda.show_contacts()
                while contact:
                    print (contact)
                    time.sleep(2)

        elif answer == "4":
            message = "👋 Goodbye!"
            print (message)
            return False
        
        else:
            print("Option not found")
            answer = input("Select an option (1-4): ")
            while answer not in ("1","2","3","4"):
                print("Option not found")
                answer = input("Select an option (1-4): ")

            

menu()