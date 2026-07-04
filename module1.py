furniture = []
def addRecord():
    flag='y'
    print("**ADDING YOUR RECORD**")
    while flag=='y':
        print()
        id=int(input("Enter Furniture's ID :"))
        if id in furniture:
            print("This id is already assigned to another item")
        else:
            furniture. append(id)
            type=input("Enter Furniture's type :")
            furniture.append(type)
            material=input("Enter Furniture's material :")
            furniture.append(material)
            price=int(input("Enter Furniture's price :"))
            furniture.append(price)
            flag = input("Enter y to continue adding records: ")
def viewRecord():
    print("\nwe have following record:")
    print("ID\t\tTYPE\t\tMATERIAL\t\tPRICE")
    for i in range(0,len(furniture),4):
        print(furniture[i],"\t\t",furniture[i+1],"\t\t",furniture[i+2],"\t\t",furniture[i+3])

def searchRecord():
    check='y'
    while check=='y':
        searchid=int(input("enter id you wanna search : "))
        if searchid in furniture:
            for i in range(0,len(furniture),4):
                if searchid==furniture[i]:
                    print("ID = ",furniture[i])
                    print("Type = ", furniture[i+1])
                    print("Material = ", furniture[i+2])
                    print("Price = ", furniture[i+3])
            check=input("Enter y if you want to check again : ")
        else:
            print("Record not found")
            flag=int(input("Press 1 to search again or zero to exit"))
            if flag==0:
                break


def updateRecord():
    check='y'
    flag=0
    while check=='y':
        updatef=int(input("Enter furniture id you want to update : "))
        if updatef in furniture:
            for i in range(0,len(furniture),4):
                if updatef==furniture[i]:
                    print("Current information regarding this id is : ")
                    print("1.Type=",furniture[i+1],", 2.Material=",furniture[i+2],", 3.Price=",furniture[i+3])
                    choice1=int(input("What you want to update : "))
                    if choice1==1:
                        furniture[i+1]=input("Enter new furniture type: ")
                    elif choice1==2:
                        furniture[i+2]=input("Enter new material : ")
                    elif choice1==3:
                        furniture[i+3]=input("Enter new price : ")
                    print(" data updated successfully")
            check=input("Enter y if want to update more ")
        else:
            print("Record not found")
            flag=int(input("Press 1 to enter ID again or zero to exit"))
            if flag==0:
                break








