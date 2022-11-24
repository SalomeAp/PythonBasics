# Homework #1
# Lecturer: Akmal Husanov
# Student: Salome Aptsiauri
# Date: 10/17/2022

# 3-4 and 3-5
Guests = ['John Lennon', 'Plato', 'nietzsche']
print(Guests[-1].title() + "," + "\t" + 'I would like to invite you on dinner' + "\n Please, come by 8 o'clock")
print(Guests[0].title() + "," + "\t" + 'I would like to invite you on dinner' + "\n Please, come by 8 o'clock")
print(F"{Guests[1].title()} \t I would like to invite you on dinner \n Please, come by 8 o'clock")
Removed_Guest = Guests.pop(-1)
print(Guests[-1])
print(Removed_Guest)
print(f"{Removed_Guest} : Can't Make it Tonight")
Guests.append('Socrates')
print(F"{Guests[-1].title()} , \t I would like to invite you on dinner \n Please, come by 8 o'clock")
Guests.insert(0, 'Kant')
print(Guests)
print(F"{Guests[0].title()} , \t I would like to invite you on dinner \n Please, come by 8 o'clock")
# ======================================================================================================================================
# Exercise 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end of your program informing people that you found a  bigger dinner table.
print(f'{list(Guests)} I want to inform you that i found a bigger table and I can invite more people')
# • Use insert() to add one new guest to the beginning of your list.
Guests.insert(0, 'Mamardashvili')
#• Use insert() to add one new guest to the middle of your list.
Guests.insert(-3, 'Darwin')
# • Use append() to add one new guest to the end of your list.
Guests.append('Homer')
philosopher = Guests
#• Print a new set of invitation messages, one for each person in your list.
for philosopher in Guests:
    print(f'{philosopher} I would be honored to see you on my dinner party, tomorrow by 8pm. \n Disclaimer:Formal attire is not required')
#==================================================================================================================================
# 3.7 Shrinking Guests list
#Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
for philosopher in Guests:
    print(f'{philosopher} I was just informed that the bigger table is currently is reserved and i will be able to invite only two of you')
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite  them to dinner.
removed_Guest = (Guests.pop(0), Guests.pop(1), Guests.pop(2), Guests.pop(3), Guests.pop(-1))
a = removed_Guest
for a in removed_Guest:
    print(f'{a} \t I deeply sorry to inform you that i can not invite you on dinner, because of the size of the table')
print(Guests)
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
b = Guests
for b in Guests:
    print(f'{b} I am honored to inform you that you are still invited on my dinner party')
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end
# of your program.
del Guests[0]
del Guests[-1]
print(Guests)
#================================================================================
# 3.8 Seeing the world
#    .Store the locations in a list. Make sure the list is not in alphabetical order.
Places = ['Japan', 'Alaska', 'New Zealand', 'Austria', 'Switzerland']
Places.sort()
print(Places)
#    .Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
Places = ['Japan', 'Alaska', 'New Zealand', 'Austria', 'Switzerland']
print(Places)
#    • Use sorted() to print your list in alphabetical order without modifying the actual list.
#    • Show that your list is still in its original order by printing it.
Places_Alphabetical = sorted(Places)
print(Places_Alphabetical)
print(Places)
# • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
Places_Alphabetical = sorted(Places,reverse=True)
print(Places_Alphabetical)
print(Places)
# • Use reverse() to change the order of your list. Print the list to show that its order has changed.
Places.reverse()
print(Places)
#  • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
Places.reverse()
print(Places)
#  • Use sort() to change your list so it’s stored in alphabetical order. Print the  list to show that its order has been changed.
#  • Use sort() to change your list so it’s stored in reverse alphabetical order.
#    Print the list to show that its order has changed.
Places.sort()
Places.sort(reverse=True)
print(Places)
#============================================================================================================
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46), use len() to print a message indicating the number
#  of people you are inviting to dinner.
Guests = ['John Lennon', 'Plato', 'nietzsche']
print(f'Question: How many guest are in total? Answer: {len(Guests)}')
#==============================================================================================================
# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#  • Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should
#  have one line of output containing a simple statement like I like pepperoni pizza.
Pizzas = ['Cheese','Veggie','Margherita']
a = Pizzas
for a in Pizzas:
    print(f'My favorite pizza is... {a}')
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
Pizzas = ['Cheese','Veggie','Margherita']
a = Pizzas
for a in Pizzas:
    print(f'My favorite pizza is... {a}')
print(f'\n Midnight thoughts about pizza: \n I really like pizza with cheese \n I have nothing against Veggie pizza too \n I think i would try Margherita pizza as well \n Ok. Now, I am hungry.')
#===============================================================================================================
#4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
#    print out the name of each animal.
#  • Modify your program to print a statement about each animal, such as A dog would make a great pet.
animals = ['tiger','Cat','Cheetah']
a = animals
for a in animals:
    print(f'I think a {a} would make a greap pet!')
# • Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!
animals = ['tiger','Cat','Cheetah']
a = animals
for a in animals:
    print(f'I think a {a} would make a greap pet!')
print(f'Any of these animals would make great pet!')
#===============================================================================================================
# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
a = range(1,21)
for a in range(1,21):
    print(f'number {a}')
#==============================================================================================================
# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)
nums = range(1,1000000)
for nums in range(1,1000000):
    print(f'number: {nums}')
#==============================================================================================================
#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
nums = range(1,1000000)
print(min(nums))
print(max(nums))
print(sum(nums))
#==============================================================================================================
# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
nums = range(1,20,2)

for nums in range(1,20,2):
    print(f'Find odd numbers: {nums}')
#===============================================================================================================
#4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
nums = range(3,30,3)

for nums in range(3,30,3):
    print(f'multiples of 3: {nums}')
#=================================================================================================================
#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
nums = range(1,11)

for nums in range(1,11):
    print(f'cubes of the numbers from 1 to 11: {nums**3}')
#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubed_numbers = []
nums = (list(range(1,11)))
for nums in range(1,11):
    cubed_numbers.append(nums**3)
    print(f'cubed_numbers')

