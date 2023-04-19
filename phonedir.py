phoneDirectory = {}#initializing an empty dictionary
print(" WELCOME TO THE GRANN'S PHONE DIRECTORY \n")#printing according to desired output
m=0
while True:# Creating a while loop to keep the program running until the user enters 5
    if m==1:
       print("Menu\n")
    m=1
    print("1. Add a record\n")      #printing for desired result
    print("2. Search a record\n")
    print("3. Update a record\n")
    print("4. Delete a record\n")
    print("5. Quit\n")

    choice = int(input("Enter your choice: ")) #asking for user input for thier choice of action
    print("\n")
    if choice == 1:
        name = input("Enter name : \n")
        if  all(na.isspace() or na.isalpha() for na in name):
            
            phone = (input("Enter phone number: \n"))
            if len(phone) ==10 and  phone.isdigit():#checking if number entered is 10 digit number and does not contain any symbols or alphabets
            
                phoneDirectory[name] = phone
                print("Record added successfully\n")
        
            else:
                print("The number is not valid, please enter a 10 digit phone number\n")
        else:
            print("please do not enter numbers in or symbols in name")   
    elif choice == 2:
        name = input("Enter name to search: \n")
        if name in phoneDirectory:
            print(f"{name} : {phone}")
        else:
            print("Record not found\n")
    elif choice == 3:
        name = input("Enter name to update: \n")
        if name in phoneDirectory:
            phone = input("Enter new phone number: \n")
            phoneDirectory[name] = phone
            print("Record updated successfully\n")
        else:
            print("Record not found\n")
    elif choice == 4:
        name = input("Enter name to delete: \n")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print("Record deleted successfully\n")
        else:
            print("Record not found\n")
    elif choice == 5:
        break
    else:
        print("Invalid choice\n")