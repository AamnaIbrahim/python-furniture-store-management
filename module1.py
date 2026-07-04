furniture = []

def addRecord():
    flag = 'y'
    print("**ADDING YOUR RECORD**")
    while flag == 'y':
        print()
        try:
            id = int(input("Enter Furniture's ID :"))
        except ValueError:
            print("Invalid ID! Please enter a number.")
            continue

        if id < 0:
            print("ID cannot be negative!")
            continue

        if id in furniture:
            print("This id is already assigned to another item")
        else:
            try:
                type = input("Enter Furniture's type :")
                material = input("Enter Furniture's material :")
                price = float(input("Enter Furniture's price :"))
            except ValueError:
                print("Invalid price! Please enter a number.")
                continue

            if price < 0:
                print("Price cannot be negative!")
                continue

            furniture.append(id)
            furniture.append(type)
            furniture.append(material)
            furniture.append(price)

        flag = input("Enter y to continue adding records: ")


def viewRecord():
    print("\nwe have following record:")
    print("ID\t\tTYPE\t\tMATERIAL\t\tPRICE")
    try:
        for i in range(0, len(furniture), 4):
            print(furniture[i], "\t\t", furniture[i+1], "\t\t", furniture[i+2], "\t\t", furniture[i+3])
    except IndexError:
        print("Error displaying records: data appears to be corrupted.")


def searchRecord():
    check = 'y'
    while check == 'y':
        try:
            searchid = int(input("enter id you wanna search : "))
        except ValueError:
            print("Invalid ID! Please enter a number.")
            continue

        if searchid in furniture:
            for i in range(0, len(furniture), 4):
                if searchid == furniture[i]:
                    print("ID = ", furniture[i])
                    print("Type = ", furniture[i+1])
                    print("Material = ", furniture[i+2])
                    print("Price = ", furniture[i+3])
            check = input("Enter y if you want to check again : ")
        else:
            print("Record not found")
            try:
                flag = int(input("Press 1 to search again or zero to exit"))
            except ValueError:
                print("Invalid input, exiting search.")
                break
            if flag == 0:
                break


def updateRecord():
    check = 'y'
    while check == 'y':
        try:
            updatef = int(input("Enter furniture id you want to update : "))
        except ValueError:
            print("Invalid ID! Please enter a number.")
            continue

        if updatef in furniture:
            for i in range(0, len(furniture), 4):
                if updatef == furniture[i]:
                    print("Current information regarding this id is : ")
                    print("1.Type=", furniture[i+1], ", 2.Material=", furniture[i+2], ", 3.Price=", furniture[i+3])
                    try:
                        choice1 = int(input("What you want to update : "))
                    except ValueError:
                        print("Invalid choice! Please enter a number.")
                        continue

                    try:
                        if choice1 == 1:
                            furniture[i+1] = input("Enter new furniture type: ")
                        elif choice1 == 2:
                            furniture[i+2] = input("Enter new material : ")
                        elif choice1 == 3:
                            new_price = float(input("Enter new price : "))
                            if new_price < 0:
                                print("Price cannot be negative!")
                                continue
                            furniture[i+3] = new_price
                        else:
                            print("Invalid option")
                            continue
                    except ValueError:
                        print("Invalid price! Please enter a number.")
                        continue

                    print(" data updated successfully")
            check = input("Enter y if want to update more ")
        else:
            print("Record not found")
            try:
                flag = int(input("Press 1 to enter ID again or zero to exit"))
            except ValueError:
                print("Invalid input, exiting update.")
                break
            if flag == 0:
                break
