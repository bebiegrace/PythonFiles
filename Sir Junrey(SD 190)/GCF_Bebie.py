print("Greatest Common Factor(GCF)")
print("Welcome!!!")
print("=============================================================")
print("Find the Greatest Common Factor of the two numbers!")

def compute_gcf(x, y):


    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcf = i 
    return gcf
while True:
    num1 = int(input("Enter 1st number: ")) 
    num2 = int(input("Enter 2nd number: "))

    print("__________________________________________________________________")
    print("The Greatest Common Factor  is", compute_gcf(num1, num2))
    ask = str(input("Do you want to continue(Y/n)?:"))
    if ask == "Y" or ask == "y":
        continue
    else:
        break


        