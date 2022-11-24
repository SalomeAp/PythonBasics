#  5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.

user_names = []
for user in user_names:
    if user == "admin":
        print(F"{user} Hello admin, Would you like to see status report?")
    elif user != "admin":
        print(f"Hello {user}, thank you for logging in again")
    else:
        print('We need to find some users!')

#  5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.

current_users = ['John', 'Elsa','Anna','Spiderman']
new_users = ['Bob','Max','Eleonor','John','Anna']
for user in new_users:
    if user in current_users:
        print(f"{user} has to create new username")
    else:
        print(f"{user} is avalaible")

#  5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
#
# • Use an if-elif-else chain inside the loop to print the proper ordinal end-
# ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
#
# 7th 8th 9th", and each result should be on a separate line.

nums = range(1,10)
for a in nums:
    if a == 1:
        print(f"{a}st ")
    elif a == 2:
        print(f"{a}nd")
    elif a == 3:
        print(f"{a}rd")
    else:
        print(f"{a}th")




