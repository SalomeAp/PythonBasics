from typing import List, Any, Type

Places = ['Japan', 'Ibiza', 'Hawaii', 'Tbilisi']
for a in Places:
    a = (a + "\nHappy")
    print(f'I want to visit {a.title()} next year')
    print(a)

for num in range(5):
    print(f'Each number individualy', {num})

for num in range(21, 36, 4):
    print(num)
Num_quartered: list[Any] = [ ]
for Num1 in range(25, 30):
    print(f'squared number', {Num1 ** 2})
    Num_quartered.append(Num1 ** 2)
    print(f'quartered number list:', {Num_quartered})


#What are the square numbers between 25 and 30


for num2 in range(25,30):
    print(f'num2 is {num2} and Squared number is {num2**2}')