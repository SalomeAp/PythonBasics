# functions chapt 7
from typing import Dict, Any


def greet_user():
    print("Hello Class!")
    print("Wonderful sunny day today!")


"""8-1. Message: Write a function called display_message() that prints one sentence
 telling everyone what you are learning about in this chapter. Call function, and make sure the message displays correctly."""


def display_message():
    print("I've learned that def is the function, that helps to create new function")


display_message()

"""8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call."""

"""8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""


def make_shirt(size, msg):
    print(f"I have a shirt size {size} which says {msg}")


make_shirt("M", "Nirvana")
make_shirt(msg="Nirvana", size="M")

"""8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""


def make_shirt(size="L", msg="I LOVE PYTHON"):
    print(f"I have a shirt size {size} which says {msg}")


make_shirt()

"""8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country."""


def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}")


describe_city(city="tbilisi")

"""8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that???s returned."""


def city_country(city: str, country: str):
    return f"{city.title()} is in {country.title()}"


location = city_country("tbilisi", "Georgia")
print(location)

"""8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the

number of tracks on an album. If the calling line includes a value for the num-
ber of tracks, add that value to the album???s dictionary. Make at least one new

function call that includes the number of tracks on an album."""


def make_album(name, album):
    track = {name: "title", album: "song"}
    return track




"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album???s artist and title. Once you have that
information, call make_album() with the user???s input and print the dictionary
that???s created. Be sure to include a quit value in the while loop."""


def make_it(name, album):
    track = {name: "singer", album: "song"}
    return track

is_true = []
while is_true != "n":
    print("\nPlease enter singer and song")
    name = input("singer:  ")
    album = input("song: ")
    print(F"Name your favorite artist {make_it(name)} and a song {make_it(album)}")
    is_true = input("Do you want to quit? y/n ")
