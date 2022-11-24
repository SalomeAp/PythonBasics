# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
from typing import List

flower = "daisy"
print("Is flower == 'daisy'? I predict True ")
print(flower == 'daisy')
print("\nIs flower == 'violet'? I predit false")
print(flower == 'violet')
pizza = "Mushroom"
print("\nIs pizza == 'Mushroom'? I predit True ")
print(pizza == 'Mushroom')
print('\nIs pizza =="Pepperoni? I predit False')
print(pizza == "pepperoni")
print('\nIs pizza =="Cheese" I predit false')
nuts = "walnut"
print('\nIs nut == "walnut"? I predit True')
print(nuts == 'walnut')

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:

# • Tests for equality and inequality with strings
# • Tests using the lower() function
car = 'Mercedes'
print(f" I love Mercedes. It's {car.lower() == 'mercedes'}")
# • Tests using the and keyword and the or keyword
print("===")
num = 1
num1 = 3
print(f'I only have 1 brother. Is that true? {num >= 0 or num < 3}')
print(f"I only have three best friend. Is that true? {num1 >= 0 and num1 < 4}")
print('========================================')
# • Test whether an item is in a list
My_besties = ['Natia', 'Shorena', 'Maka']
friend = 'Natia'
if friend not in My_besties:
    print(f"Let's see what future holds")
else:
    print(f"I love and miss my girl")
# • Test whether an item is not in a list
friend1 = 'Helen'
if My_besties != friend1:
    print(f"Let's see what future holds")
else:
    print(f"I love and miss my girl")
# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
alien_color = ['green', 'yellow', 'red']
if alien_color == 'green':
    print(f'Player just earned 5 points')
# Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)
if 'green' in alien_color:
    print(f'Player just earned 5 points')  # pass
elif alien_color != 'green':
    print("blank")

if 'neon' in alien_color:
    print(f'player did not earn 5 points')  # fail
elif 'purple' in alien_color:
    print(f'player earned 5 points')

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print(f'Player just earned 5 points shooting an alien')
# • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
alien_color = ['green', 'yellow', 'red']
for color in alien_color:
    if color == 'green':
        print(f'Player just earned 5 points shooting an alien')
    else:
        print(F"player earned 10 points")
# • Write one version of this program that runs the if block and another that runs the else block.
if 'green' in alien_color:
    print(f'Player just earned 5 points shooting an alien')  # if block pass
else:
    print("don't print anything")
# =====================
if 'purple' in alien_color:
    print(f'Player just earned 5 points shooting an alien')  # else block pass
else:
    print("don't print anything")
# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
for color in alien_color:
    if color == "green":
        print(f'Player who shot {color} alien, 5 points shooting an alien')
    elif color == "yellow":
        print(F"player who shot {color} alien,earned 10 points")
    elif color == "red":
        print(F"player who shot {color} alien, earned 15 points")
# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is a baby.
# • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# • If the person is age 65 or older, print a message that the person is an elder.

age = 25
if age < 2:
    print("This person is a baby")
elif 2 <= age < 4:
    print("this person is a toddler")
elif age >= 4 and age <13:
    print("This person is a kid")
elif age >= 13 and age < 65:
    print("This person is an adult")
elif age >= 65:
    print(" This person is an elder")

#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
#independent if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.
#• Write five if statements. Each should check whether a certain kind of fruit
#is in your list. If the fruit is in your list, the if block should print a statement,such as You really like bananas!
Favorite_fruits = ['apple','banana','plum']
for fruit in Favorite_fruits:
    if fruit == "banana":
        print(f"I really like {fruit}")
    elif fruit == "apple":
        print(f"I really like {fruit}")
    elif fruit == "plum":
        print(f"I really like {fruit}")
# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
#
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for log-
# ging in again.
user_names = ["eric","admin","sudo","editor","salome"]
for user in user_names:
    if user == "admin":
        print(F"{user} Hello admin, Would you like to see status report?")
    else:
        print(f"Hello {user}, thank you for logging in again")
