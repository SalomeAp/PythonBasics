# Homework #2
# Lecturer: Akmal Husanov
# Student: Salome Aptsiauri
# Date: 10/21/2022

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program’s list.

# Question: it doesn't exclude last one when i print and slice list

Places = ['Japan', 'Alaska', 'New Zealand', 'Austria', 'Switzerland']
print(Places[0:3])
# • Print the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
Places = ['Japan', 'Alaska', 'New Zealand', 'Austria', 'Switzerland']
print(Places[2:4])
# • Print the message, The last three items in the list are:. Use a slice to print the last three items in the list.
Places = ['Japan', 'Alaska', 'New Zealand', 'Austria', 'Switzerland']
print(Places[2:])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following: •• Add a new pizza to the original list.
Pizzas = ['Cheese', 'Veggie', 'Margherita']
friend_pizzas = Pizzas[:]
print(friend_pizzas)
Pizzas.insert(1,"mushroom")
#• Add a different pizza to the list friend_pizzas.
friend_pizzas.append("Pepperoni")
print(friend_pizzas)
# Prove that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

for pizza in Pizzas:
    print(f'My favorite pizzas are: {pizza}')
print('======================================')
for pizza in friend_pizzas:
    print(f'My favorite pizzas are: {pizza}')

#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for food in my_foods:
    print(f'my favorite foods are: {my_foods}')
print('\n')
for food in friend_foods:
    print(f'my friend favorite foods are: {friend_foods}')

