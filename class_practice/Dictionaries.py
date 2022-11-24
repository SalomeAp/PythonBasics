
#  6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
person = { "first_name": "Shorena",
           "last_name": "Maisuradze",
           "age": 27,
           "city": "Tbilisi",
           "country":"Georgia"}
print(f"My friends's name is {person['first_name']}")
print(f"My friends's last name is {person['last_name']}")
print(f"My friends's age is {person['age']}")
print(f"My friends lives in {person['city']}")

#  6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.


fav_nums = {'Natia': 9,'Shoke': 10, 'maka': 11, "lasha": 12, "uta": 13}
print(f"Natia's favorite number is: {fav_nums['Natia']}")
print(f"Shoke's favorite number is: {fav_nums['Shoke']}")
print(f"Maka's favorite number is: {fav_nums['maka']}")
print(f"Lasha's favorite number is: {fav_nums['lasha']}")
print(f"Utas's favorite number is: {fav_nums['uta']}")

#  6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

Python_glossary = {"indentation": "the space at the beginning of a line ",
                   "whitespace":"\n\t characters that allow you to make the code easily readable",
                   "list": "data structure, that allows you to store multiple values in a single variable",
                   "dictionary": "data structure, that creates keys and elements",
                   "string": "data type, unicode characters"}
print(f"let's find out what each python programming word means ")
print(f" programming word whitespace meaning: {Python_glossary['whitespace']}")
print(f" programming word list meaning: {Python_glossary['list']}")
print(f" programming word dictionary meaning: {Python_glossary['dictionary']}")
print(f" programming word string meaning: {Python_glossary['string']}")

