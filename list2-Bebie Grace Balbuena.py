
#Mang tatoy want to automate its balut business. 
#Balut comes in different variant (#16, #18, and penoy).
#Create a program that would help a simple POS (Point of sales) program that would allow to accept customer name, total balut orders from multiple variants and ask for the total payment. 
#The program should display a simple receipt showing the customer name, the orders with the corresponding amount, total amount, paid amount and the change. 
#The program should be able to accommodate more than 1 customer. 
#When the program ends it will show the total number of customers and the sales for the day. 

customer = {}

balut = {"#16":25, "#18":30, "Penoy":10,}



def add_customer():
    name = input("First Customer's Name: ")
    no_16 = input("How many #16 price(25) : ")
    no_18 = input("How many #18 price(30) : ")
    penoy = input("How many penoy price(10) : ")
    total = (balut.get("#16") * int(no_16))+(balut.get("#18") * int(no_18))+(balut.get("Penoy") * int(penoy))
    customer[name] = total
    print("\nYour Total: ",total)
    cash = input("\nCash: ")
    change = int(cash) - total
    
    print("\nOfficial Receipt")
    print("Customer's Name: ",name,"\nTotal:       Php%8.2f"%(int(total)),"\nCash : Php%8.2f"%(int(cash)),"\nChange: Php%8.2f"%(int(change)))
    
    
name = input("Second Customer's Name: ")
no_16 = input("How many #16 price(25) : ")
no_18 = input("How many #18 price(30) : ")
penoy = input("How many penoy price(10) : ")
total = (balut.get("#16") * int(no_16))+(balut.get("#18") * int(no_18))+(balut.get("Penoy") * int(penoy))
customer[name] = total
print("\nYour Total: ",total)
cash = input("\nCash: ")
change = int(cash) - total
    
print("\nOfficial Receipt")
print("Customer's Name: ",name,"\nTotal:       Php%8.2f"%(int(total)),"\nCash : Php%8.2f"%(int(cash)),"\nChange: Php%8.2f"%(int(change)))
    
print("=====================================")

print("Total Costumers: 2 costumers")