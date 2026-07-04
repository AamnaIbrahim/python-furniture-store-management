customer = []

def addCustomer():
    flag = 'y'
    print("**ADDING YOUR RECORD**")
    while flag == 'y':
        print()
        try:
            id = int(input("Enter customers's CNIC :"))
        except ValueError:
            print("Invalid CNIC! Please enter a number.")
            continue

        if id in customer:
            print("This cnic is already registered try another one")
        else:
            try:
                name = input("Enter customer's name :")
                phone = int(input("Enter customer's phone number :"))
                age = int(input("Customers age : "))
            except ValueError:
                print("Invalid phone number or age! Please enter numbers only.")
                continue

            customer.append(id)
            customer.append(name)
            customer.append(phone)
            customer.append(age)

        flag = input("Enter y to continue adding records: ")


def viewCustomer():
    print("CNIC\t\tNAME\t\tPHONE NUMBER\t\tAGE")
    try:
        for i in range(0, len(customer), 4):
            print(customer[i], "\t\t", customer[i+1], "\t\t", customer[i+2], "\t\t", customer[i+3])
    except IndexError:
        print("Error displaying records: data appears to be corrupted.")


def searchCustomer():
    check = 'y'
    while check == 'y':
        try:
            searchid = int(input("enter id you wanna search : "))
        except ValueError:
            print("Invalid ID! Please enter a number.")
            continue

        if searchid in customer:
            for i in range(0, len(customer), 4):
                if searchid == customer[i]:
                    print("ID = ", customer[i])
                    print("name = ", customer[i+1])
                    print("phone number = ", customer[i+2])
                    print("Age = ", customer[i+3])
                    check = input("Enter y if you want to check again : ")
        else:
            print("Record not found search again")
            check = input("Enter y to search again or any key to stop: ")


def updateCustomer():
    check = 'y'
    while check == 'y':
        try:
            updatec = int(input("Enter customer id you want to update : "))
        except ValueError:
            print("Invalid ID! Please enter a number.")
            continue

        if updatec in customer:
            for i in range(0, len(customer), 4):
                if updatec == customer[i]:
                    print("Current information regarding this id is : ")
                    print("1.name=", customer[i+1], ", 2.phone number=", customer[i+2], ", 3.age=", customer[i+3])
                    try:
                        choice1 = int(input("What you want to update : "))
                    except ValueError:
                        print("Invalid choice! Please enter a number.")
                        continue

                    try:
                        if choice1 == 1:
                            customer[i+1] = input("Enter new name : ")
                        elif choice1 == 2:
                            customer[i+2] = int(input("Enter phone number : "))
                        elif choice1 == 3:
                            customer[i+3] = int(input("Enter new age : "))
                        else:
                            print("Invalid option")
                            continue
                    except ValueError:
                        print("Invalid phone number or age! Please enter numbers only.")
                        continue

                    print(" data updated successfully")
            check = input("enter y if want to update more : ")
        else:
            print("Record not found")
            check = input("enter y to try again or any key to stop: ")
