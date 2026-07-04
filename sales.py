from module1 import *
from module2 import *
sales = []

def addSales():
    check = 'y'
    while check == 'y':
        try:
            cid = int(input("Enter customer's CNIC : "))
        except ValueError:
            print("Invalid CNIC! Please enter a number.")
            continue

        if cid in customer:
            sales.append(cid)
            for i in range(0, len(customer)):
                if cid == customer[i]:
                    sales.append(customer[i+1])
                    sales.append(customer[i+2])
                    sales.append(customer[i+3])

            try:
                fid = int(input("Enter the furniture id you want to buy : "))
            except ValueError:
                print("Invalid furniture ID! Please enter a number.")
                # remove the customer info we just added since the sale wasn't completed
                del sales[-4:]
                continue

            if fid in furniture:
                sales.append(fid)
                for i in range(0, len(furniture)):
                    if fid == furniture[i]:
                        sales.append(furniture[i+1])
                        sales.append(furniture[i+2])
                        sales.append(furniture[i+3])
                        print("your order is booked!")
                        check = input("enter y if you want to order more")
            else:
                print("This furniture id doesn't exists")
                del sales[-4:]
                break
        else:
            print("this customer id doesn't exists ")
            break


def viewsales():
    try:
        for i in range(0, len(sales), 8):
            print()
            print("customer Info:")
            print("customerCnic\t\tCustomerName\t\tphonenumber\t\tage")
            print(sales[i], "\t\t\t", sales[i+1], "\t\t\t", sales[i+2], "\t\t", sales[i+3])
            print("Furniture Booked by this customer : ")
            print("FurnitureId\t\tType\t\tMaterial\t\tPrice")
            print(sales[i+4], "\t\t", sales[i+5], "\t\t", sales[i+6], "\t\t", sales[i+7])
    except IndexError:
        print("Error displaying sales: data appears to be corrupted.")


def searchsale():
    check = 'y'
    while check == 'y':
        try:
            cid = int(input("Enter customer id from which your order is booked : "))
        except ValueError:
            print("Invalid ID! Please enter a number.")
            continue

        found = False
        for i in range(0, len(sales), 8):
            if cid == sales[i]:
                found = True
                print("Your order details are as follows : ")
                print("Customer Id : ", sales[i])
                print("customer name : ", sales[i+1])
                print("customer phone no : ", sales[i+2])
                print("customer age : ", sales[i+3])
                print("Furniture id : ", sales[i+4])
                print("Furniture type : ", sales[i+5])
                print("Furnitures material : ", sales[i+6])
                print("Price : ", sales[i+7])

        if not found:
            print("This id is not available")

        check = input("Enter y if you wanna search again : ")
