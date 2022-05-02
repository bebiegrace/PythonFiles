print("Least Common Multiple(LCM)")
print("Welcome!!!")
print("=============================================================")
print("Find the Least Common Multiple of the two numbers!")
def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           compute_lcm = greater
           break
       greater += 1

   return compute_lcm
while True:
    num1 = int(input("Enter 1st number: ")) 
    num2 = int(input("Enter 2nd number: "))

    print("__________________________________________________________________")
    print("The Least Common Multiple is", compute_lcm(num1, num2))

    ask = str(input("Do you want to continue(Y/n)?:"))
    if ask == "Y" or ask == "y":
        continue
    else:
        break