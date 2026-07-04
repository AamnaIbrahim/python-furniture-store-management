customer=[]
def addCustomer():
    flag='y'
    print("**ADDING YOUR RECORD**")
    while flag=='y':
        print()
        id = int(input("Enter customers's CNIC :"))
        if id in customer:
            print("This cnic is already registered try another one")
        else:
            customer.append(id)
            name = input("Enter customer's name :")
            customer.append(name)
            phone = int(input("Enter customer's phone number :"))
            customer.append(phone)
            age=int(input("Customers age : "))
            customer.append(age)
            flag=input("Enter y to continue adding records: ")

def viewCustomer():
    print("CNIC\t\tNAME\t\tPHONE NUMBER\t\tAGE")
    for i in range(0,len(customer),4):
        print(customer[i],"\t\t",customer[i+1],"\t\t",customer[i+2],"\t\t",customer[i+3])



def searchCustomer():
    check='y'
    while check=='y':
        searchid=int(input("enter id you wanna search : "))
        if searchid in customer:
            for i in range(0,len(customer),4):
                if searchid==customer[i]:
                    print("ID = ",customer[i])
                    print("name = ", customer[i+1])
                    print("phone number = ", customer[i+2])
                    print("Age = ", customer[i+3])
                    check=input("Enter y if you want to check again : ")
        else:
            print("Record not found search again")


def updateCustomer():
    check='y'
    while check=='y':
        updatec=int(input("Enter customer id you want to update : "))
        if updatec in customer:
            for i in range(0,len(customer),4):
                if updatec==customer[i]:
                    print("Current information regarding this id is : ")
                    print("1.name=",customer[i+1],", 2.hone numberp=",customer[i+2],", 3.age=",customer[i+3])
                    choice1=int(input("What you want to update : "))
                    if choice1==1:
                        customer[i+1]=input("Enter new name : ")
                    if choice1==2:
                        customer[i+2]=input("Enter phone number : ")
                    if choice1==3:
                        customer[i+3]=input("Enter new age : ")
                    print(" data updated successfully")
            check=input("enter y if want to update more : ")
        else:
            print("Record not found")




