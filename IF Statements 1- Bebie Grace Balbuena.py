#if the number is divisible by 2 print display the number and "FIZZ" 
#if the number is divisible by 5 display the number and  "BUZZ"
#if the number is both divisible by 2 and 5 display the number and "FIZZBUZZ" otherwise just display the number.

##answer

def FIZZ_BUZZ(input):

    if input % 2 ==0 and input % 5 ==0:
        return 'FIZZBUZZ'
    if input % 2 ==0:
        return "FIZZ"
    if input % 5 ==0:
        return 'BUZZ'

    return input 
    print(FIZZ_BUZZ(40))

#Take three numbers from the user and print the greatest number.

#answer

a = int(input("Enter first integer : "))
b = int(input("Enter second integer :"))
c = int(input("Enter third integer :"))
print("Maximum is ", end='')
if b <= a >=c:
    print(a)
elif a <= b >=c:
    print(b)
elif a <=c >= b:
    print(c)
    
# Write a program that keeps a number from the user and generates an integer between 1 and 7 and displays the name of the weekday.
# Taken day number from user

#answer

weekday = int(input("Enter weekday day number (1-7) : "))

if weekday == 1 :
    print("Monday")

elif weekday == 2 :
    print("Tuesday")

elif(weekday == 3) :
    print("Wednesday")

elif(weekday == 4) :
    print("Thursday")

elif(weekday == 5) :
    print("Friday")

elif(weekday == 6) :
    print("Saturday")

elif (weekday == 7) :
    print("Sunday")

else :
    print("Please enter weekday number between 1-7.")

#Write a program that takes the user to provide a single character from the alphabet. 
#Print Vowel or Consonant, depending on the user input.
#If the user input is not a letter (between a and z or A and Z), 
#if is a string of length > 1, print an error message.



val =str(input("Enter an Alphabet : "))
ch = input("Enter an Alphabet: ")
if ch in ('a','e','i','u','o','A','E','I','U','O'):
     print(ch, "is a vowel") 
if ch in ('b', 'c','d','f', 'g','h',"j",'k','l','m','n','p','q','r','s','t','v','w','x','y','z','B', 'C','D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'V', 'X','Y', 'Z'):
     print(ch, "is a consonant") 

else:
    print("Error Message")




#Enter a 3 digit number and display the smallest digit.

##answer

a = int(input("Enter a digit :"))
b = int(input("Enter a digit :"))
c = int(input("Enter a digit :"))
print("Smallest is ", end='')
if b >= a <=c:
    print(a)
elif a >= b <=c:
    print(b)
elif a >=c <= b:
    print(c)

