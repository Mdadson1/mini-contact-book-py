from enum import Enum

class State(Enum):
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

#contact 
class Contact:
    def __init__(self, name = "", phone = ""):
        self._name = name
        self._phone = phone

        if name and phone:
            self._status = State.OCCUPIED
        else:
            self._status = State.EMPTY
    
    #accessors
    def getName(self):
        return self._name
    
    def getPhone(self):
        return self._phone
    
    def isDeleted(self):
        return self._status == State.DELETED

    #mutators
    def markDeleted(self):
        self._status = State.DELETED
    
#contact_book
class Contact_Book:
    def __init__(self):
        #dict : name is key, value Contact object
        self._contacts = {}
    
    def insert(self, name, phone):
        #create the object first
        person = Contact(name, phone)
        self._contacts[name] = person
        ''' alternatively self._contacts[name] = Contact(name,phone)'''
    
    def remove(self, name):
        #search by name(key), returns -1 if not found
        result = self._contacts.pop(name, -1) #if the remove was successful

        if result == -1:
            print(f"Unable to remove '{name}.' Please try again later.")
    
    def search(self, name):
        #must verify that key(name) exists
        if name in self._contacts:
            print(f"Name: {name}\nPhone: {self._contacts[name].getPhone()}")
        else:
            print(f"{name} not found in PhoneBook.")
    
    def listContacts(self):
        if not self._contacts:
            print("PhoneBook is empty.")
        else:
            for name, contact in self._contacts.items():
                print(f"Name: {name}\tPhone: {contact.getPhone()}")

#main block
if __name__ == "__main__":
    PhoneBook = Contact_Book()
    #should show an error message
    PhoneBook.search("james")

    PhoneBook.listContacts()
    PhoneBook.remove("james")
    PhoneBook.insert("james","212-567-894")
    PhoneBook.insert("delali", "334-567-241")
    PhoneBook.listContacts()

    PhoneBook.remove("delali")
    PhoneBook.search("james")