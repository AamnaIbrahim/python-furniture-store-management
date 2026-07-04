from module1 import *
from module2 import *
from sales import *

def main():
    flag = 0
    flag2 = 0
    check = 'y'
    while check == 'y':
        print()
        print("***MENU***")
        print("1.Furniture info   2.Customer info   3.Sales info")
        try:
            choice = int(input("what you want to do : "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            check = input("enter y to go to menu or any key to exit: ")
            continue

        if choice == 1:
            print("FURNITURE INFORMATION")
            print("1.Add Record 2.View 3.Update 4.Search ")
            try:
                option = int(input("Enter your choice : "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                check = input("enter y to go to menu or any key to exit: ")
                continue

            if option >= 5:
                print("option not available")
            else:
                if option == 1:
                    flag += 1
                    addRecord()

                elif option == 2:
                    if flag == 0:
                        try:
                            flag2 = int(input("You dont have any record to view press 1 to add record or 0 to exit "))
                        except ValueError:
                            print("Invalid input!")
                            flag2 = 0
                        if flag2 == 1:
                            addRecord()
                            flag += 1
                    else:
                        viewRecord()

                elif option == 3:
                    if flag == 0:
                        try:
                            flag2 = int(input("You dont have any record to update press 1 to add record or 0 to exit "))
                        except ValueError:
                            print("Invalid input!")
                            flag2 = 0
                        if flag2 == 1:
                            addRecord()
                            flag += 1
                    else:
                        updateRecord()

                elif option == 4:
                    if flag == 0:
                        try:
                            flag2 = int(input("You dont have any record to search press 1 to add record or 0 to exit "))
                        except ValueError:
                            print("Invalid input!")
                            flag2 = 0
                        if flag2 == 1:
                            addRecord()
                            flag += 1
                    else:
                        searchRecord()

        elif choice == 2:
            flag = 0
            print("CUSTOMER INFORMATION")
            print("1.Add Record 2.View 3.Update 4.Search ")
            try:
                option = int(input("Enter your choice : "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                check = input("enter y to go to menu or any key to exit: ")
                continue

            if option == 1:
                flag += 1
                addCustomer()
            elif option == 2:
                if flag == 0:
                    print("You dont have any record")
                else:
                    viewCustomer()
            elif option == 3:
                if flag == 0:
                    print("You dont have any record yet")
                else:
                    updateCustomer()
            elif option == 4:
                if flag == 0:
                    print("You dont have any record yet")
                else:
                    searchCustomer()
            else:
                print("option not available")

        elif choice == 3:
            flag = 0
            print("SALES INFORMATION")
            print("1.Add record  2.View record   3.Search record")
            try:
                option = int(input("Enter your choice : "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                check = input("enter y to go to menu or any key to exit: ")
                continue

            if option == 1:
                flag += 1
                addSales()
            elif option == 2:
                if flag == 0:
                    print("We dont have any order yet")
                else:
                    viewsales()
            elif option == 3:
                if flag == 0:
                    print("We dont have any order yet")
                searchsale()
            else:
                print("option not available")
            check = input("enter y to go to menu or any key to exit: ")
        else:
            print("option not available")

        check = input("enter y to go to menu or any key to exit: ")

main()
