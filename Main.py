
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contacts(args, contacts):
    name, phone = args
    contacts[name] = phone
    return("Contact added")

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        print (contacts[name])
    else:
        return("There is no contuct with such name!")

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return("Contact was changed")
    else:
        return("There is no contuct with such name!")



def all_contacts(contacts):
    for name, number in contacts.items():
        print(name, number)
  

def main():
    contacts = {}
    print("Welcome to assistant bot")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close" , "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contacts(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            show_phone(args, contacts)
        elif command == "all":
            all_contacts(contacts)
        else:
            print("Invalid command")
            
if __name__ == "__main__":
    main()

