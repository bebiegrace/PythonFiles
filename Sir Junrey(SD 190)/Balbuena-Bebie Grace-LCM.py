print("Least Common Multiple(LCM)")
print("Welcome!!!")
print("=============================================================")
print("Find the Least Common Multiple of the two numbers!")
def compute_lcm(x, y): # This is to define the function.

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           compute_lcm = greater
           break
       greater += 1

   return compute_lcm # This is to end the execution of the function call and “returns” the result.
while True: #This will indicate that the loop has to run until it breaks.
    num1 = int(input("Enter 1st number: ")) #User will input the first number.
    num2 = int(input("Enter 2nd number: ")) #User will input the second number.

    print("__________________________________________________________________")
    print("The Least Common Multiple is", compute_lcm(num1, num2)) # To show the result or the least Common Multiple(LCM) of the two inputed numbers.
    

    ask = str(input("Do you want to continue(Y/n)?:")) #Will give an option if the user wants to continue or not.
    if ask == "Y" or ask == "y": # If the users will type Y/y, the program will continue, else the program will stop.
        continue # To continue the program if the users wish to repeat.
    else:
        break  # This will terminate a loop and skip to the next code...

