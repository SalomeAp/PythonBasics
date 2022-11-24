# data structure - Data to hold multiple values, manage(add, edit, remove, update,
# Python Data structure - lists, dictionary, (set, tuple)
# [10,4,35]

nums = [3, 4, 5, 6, 4]
friends = list()
names = ['mark', 'stella', "Salome"]
bool_values = [True, False, True]
print(nums)
print(names)

solo = []  # empty list /  list is considered as mutable object because we can make changes on it.

# tuple - immutable ds

# how to add, modify, remove, read through values(access each value)

print("hi" + "\t" + str(nums[-1]).title() + "\t" + names[2])

names.append("alex")  # adds new value to the ds
names.insert(0, "Araz")

# removing elements by index
del names[3]
# or
names.pop()  # if you don't mention anything it will remove last element
deleted_names = print(names.pop())  # this one shows which one was deleted
print(deleted_names)
# removing elements by value


msg = "simple message"
print(msg)
msg = "Simple Enough Message"
# My program contains
name = "Salome"
print("Hello,{0}.\nWould you like to learn some Python today?".format(name))
print(name.upper())
print(name.lower())
print(name.title())
name = "Alberth Einstein"
quote = 'A person who never made a mistake never tried anything new'
print(name.title() + " " + "once said\t" + "'" + quote + "'")
print(name.title() + " " + "once said\t" + '\n\t\'' + quote.strip() + "'")
print(name.title().lstrip() + " " + "once said\t" + '\n\t\'' + quote + "'")

a = 5
b = 3
c = 9
d = 1
e = 16
f = 2
g = 4
h = 2
print(a + b)
print(c - d)
print(round(e / f))
print(g * h)

fvt = (7)
print("This is my favorite number" + " >>" + str(fvt))

Guests = ['John Lennon', 'Plato', 'nietzsche']
print((Guests,-1) + 'I would like to invite you on dinner'+"\n Please, come by 8 o'clock")
