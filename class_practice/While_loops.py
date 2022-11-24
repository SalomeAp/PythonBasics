# chapter 7 user input and while loops

current_number = 1
while current_number <= 5:
    print('This is current number:', current_number)
    current_number += 1

print("_______ Fuzz Buzz example with while loop ___________")
answer = ''
while (answer.lower() != 'n') and (answer.lower() != 'no'):
    # n == n -> True, n != n -> False , y != n -> True, '' != n -> True
    num = int(input('Please enter a number: '))
    # num = 3
    if num != 0:
        if num % 3 == 0 and num % 5 == 0:
            print('FuzzBuzz')
        elif num % 3 == 0:
            print('Fuzz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print('This is not dividable by 3 or 5')
    else:
        print("please enter different number than 0")
    answer = input("Do you want to continue? y/n: ")