#Pizzas: Think of at least three kinds of your favorite pizza. 
#Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza.
#For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
#The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizzas = ['pepperoni', 'hawaiian', 'Chicago']
for pizza in pizzas:
    print(pizza)
    print("\n")
for pizza in pizzas:
    print("I really like " + pizza + " pizza!")

print("\nI really love pizza!")


# 2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# Modify your program to print a statement about each animal, such as A dog would make a great pet.
# Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!

animals = ["Cow", "Bird", "Butterfly"]

for animal in animals:
    print(animal + " brave and beutiful!")
    
print("Any of these animals have the same characteristics like bieng brave.")

# 3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.

for num in range(1,21):
    print(num)



# 4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing.

for num in range(1,1000001):
    print(num)

# 5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = [num for num in range(1,21,2)]

for num in odd_numbers:
    print(num)


# 7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

threes = list(range(3, 31, 3))

for number in threes:
    print(number)

# 8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

# 9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)





