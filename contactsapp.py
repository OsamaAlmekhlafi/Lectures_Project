
# *BY Osama Abdo Modhish*
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added successfully!")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def update_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def view_all_contacts():
    if contacts:
        for name, phone in contacts.items():
            print("\nName:" + name)
            print("Phone:" + phone +"\n")
            print("---------------------")
    else:
        print("No contacts found.")

def main():
    while True:
        print("\n********** Welcome To Contacts Phone Application **********")
        print("1. Add Contact")       
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("\nEnter your choice Please (1 ---=> 5):  ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(name, phone)
        elif choice == "2":
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == "3":
            name = input("Enter contact name to update: ")
            new_phone = input("Enter new phone number: ")
            update_contact(name, new_phone)
        elif choice == "4":
            view_all_contacts()
        elif choice == "5":
            print("Thank you for using Contacts Phone. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()