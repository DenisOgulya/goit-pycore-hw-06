from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
    # def get_name(self):
    #     return self.value
    
class Phone(Field):
    def __init__(self, phone):
        if(phone.len() == 10):
            super().__init__(phone)
        #HERE SHOULD BE ERROR
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        
        self.phones.append(Phone(phone)) # реалізація класу

    def remove_phone(self, phone):
        new_phone_list = []
        for el in self.phones:
            if el.value != phone:
                new_phone_list.append(el)
        self.phones = new_phone_list
    
    def find_phone(self, phone_for_find):
         
        for phone in self.phones:
            if phone.value == phone_for_find:
                return phone.value
    
    def edit_phone(self, current_phone, new_phone):
        
        for phone in self.phones:
            if phone.value == current_phone:
                phone.value =  new_phone 
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        self.data.pop(name)


  

def main():
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    name = john_record.name.value

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    john = book.find('John')
    john.edit_phone("1234567890", "1112223333")

    found_phone = john.find_phone("5555555555")
    john.remove_phone("5555555555")

    # Видалення запису Jane
    book.delete("Jane")
    
    if __name__ == "__main__":
        main()   
    
    # contacts = {}
    # print("Welcome to assistant bot")
    # while True:
    #     user_input = input("Enter a command: ")
    #     command, *args = parse_input(user_input)
        
    #     if command in ["close" , "exit"]:
    #         print("Good bye!")
    #         break
    #     elif command == "hello":
    #         print("How can I help you?")
    #     elif command == "add":
    #         print(add_contacts(args, contacts))
    #     elif command == "change":
    #         print(change_contact(args, contacts))
    #     elif command == "phone":
    #         show_phone(args, contacts)
    #     elif command == "all":
    #         all_contacts(contacts)
    #     else:
    #         print("Invalid command")
      
# def parse_input(user_input):
#     cmd, *args = user_input.split()
#     cmd = cmd.strip().lower()
#     return cmd, *args

# def add_contacts(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     return("Contact added")

# def show_phone(args, contacts):
#     name = args[0]
#     if name in contacts:
#         print (contacts[name])
#     else:
#         return("There is no contuct with such name!")

# def change_contact(args, contacts):
#     name, phone = args
#     if name in contacts:
#         contacts[name] = phone
#         return("Contact was changed")
#     else:
#         return("There is no contuct with such name!")


      



