"""10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter."""
from logging import exception

filename1 = '../Data/Learning_Python.txt'

"""Write a program that reads the file and prints what you wrote three times.
 Print the contents once by reading in the entire file,"""
with open(filename1, "r") as learning_material:
    print(learning_material.read())

"""once by looping over the file object, """
with open(filename1, "r") as learning_material:
    for line in learning_material:
        print(line.rstrip())
"""and once by storing the lines in a list and then working with them outside the with block."""
with open(filename1, "r") as learning_material:
    line1 = learning_material.readline()
    line2 = learning_material.readline()
    line3 = learning_material.readline()
    line4 = learning_material.readline()

    all_lines = learning_material.readlines()
    print(all_lines)

all_info = ''
for line in all_lines:
    all_info += line.rstrip()

print(all_info)
print(len(all_info))

"""10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen."""
try:
    with open(filename1, "r") as learning_material:
        line1 = learning_material.readline()
        line1.replace("Python", "Java")
        print(line1)
        line2 = learning_material.readline()
        line3 = learning_material.readline()
        line4 = learning_material.readline()
except exception:
    print('Something is wrong in the code!')

"""10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt."""
filename2 = "../Data/guest.txt"
with open(filename2, "w") as guest_info:
    filename = input(str(guest_info))
    for info in guest_info:
        print(f"name: {info}")



