#The function should accept a year. 
def CheckLeap(Year):
  #Determine and display if the year is a leap year or not. 
  #(A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.)
  
##Aswer

  if((Year % 4 == 0) or  
     (Year % 100 == 0) and  
     (Year % 400 == 0)):   
    print("This is a leap Year")  
  else:  
    print ("This is not a leap Year")  
    
Year = int(input("Enter the number: "))  
CheckLeap(Year)

# If an integer variable's current number is odd, change its value so that it is now 3 times the current number plus 1
# otherwise, change its value so that it is now half of the current number (rounded down when the current number is odd). 
# Display the original number and result.

##Answer

a = int(input(" Do you want to know the new value of an odd number when it is multiplied by 3 plus 1 or an even number that is divided by 2 of the current number? Well try to enter a number: "))

if a % 2 == 1:
    print(a *3 +1, " is the new value of the current number. ")
else:
    print(a // 2, " is the result. ")


# If integer variable opCode has the value 1, read in double values for X and Y and calculate and print their sum. 

##Answer

opCode = int(input( " Enter an integer: "))

if opCode == 1:
    print(" Sum is " , opCode , "X" + "Y")
 

# If the character variable taxCode is ’T’, increase the price by adding the tax rate percentage of the price to it. Display the original and adjusted price (if there is).

##Answer

price = int(input( "Enter a variable: "))

if price == 100:
    if price < 100:
        print( price + price * price // 100)
elif price > 100:
    print( price + price * price // 100)

# Calculate the cost based on the given distance.
# Assign a value to double variable cost depending on the value of integer variable distance as follows:
# Distance: 
#    0 through 100 
#    More than 100 but not more than 500 
#    More than 500 but less than 1,000
#    1,000 or more
# Cost:
#    5.00
#    8.00
#    10.00
#    12.00

##Answer

a = int(input(" Enter a distance of 0 through 100: "))
b = int(input(" Enter a distance that is more than 100 but not more than 500: "))
c = int(input(" Enter a distance that is more than 500 but less than 1000: "))
d = int(input(" Enter a distance of 1000 or more: "))

if a >= 0 <=100:
    print( " 5.00 is the cost ")
if a > 100:
    print( a *2, " is the cost" )
if b >=100 <= 500:
    print(" 8.00 is the cost ")
if b > 500:
    print( b *2, " is the cost ")
if c > 500 <= 1000:
    print(" 10.00 is the cost ")
if c > 1000:
    print( c *2, " is the cost ")
if d >= 1000:
    print( " 12.00 is the cost ")
if d > 1000:
    print( d *2, " is the cost ")

    