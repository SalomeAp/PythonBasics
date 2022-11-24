# if number dividable by 3 print "Fuzz", if number dividable by 5 then print "Buzz,
#       if number dividable by 3 and 5 then print "FuzzBuzz" from typing import List
num = 15
if  num % 3 == 0:
    print("Fuzz")
elif num % 5 == 0:
    print("buzz")
elif num % 3 == 0 and num % 5 == 0:
    print("FuzzBuzz")

# Problem 2:
# how can you loot through the list of numbers and check that number 5 is in the list,
# when you find 5 then stop the loop print 'Hoooraa'
# Hint: use 'break' keyword to stop the loop

nums = [1, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num == 5:
        print("Hooraah")
    elif num >= 5:
        break
