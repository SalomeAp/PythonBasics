"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of

information, and a method called open_restaurant() that prints a message
indicating that the restaurant is open.

Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods."""
import privileges as privileges


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            F"Name of the restaurant is: {self.restaurant_name} and they serve {self.cuisine_type}!\n "
            F"I definitely recommend it!\n")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is Open from 5pm to midnight!\n")


chinese = Restaurant("China Wok", "Chinese")
chinese.restaurant_name
chinese.cuisine_type
chinese.describe_restaurant()
chinese.open_restaurant()

"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance."""

italian = Restaurant("Cuchina", "italian")
italian.describe_restaurant()
Mexican = Restaurant('Mexico', 'mexican')
Mexican.describe_restaurant()
print("--------------------------------------------------------------------")

"""9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user."""


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User Personal Information:\n"
              f"First Name: {self.first_name}\n"
              f"Last Name: {self.last_name}")

    def greet_user(self):
        print(f"\nHello, {self.first_name} {self.last_name}! Welcome to our website!\n")


user1 = User("Maria", "Vilanova")
user2 = User("John", "Davos")
user3 = User("Daenerys", "Targarien")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

"""9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment

the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a

day of business."""


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(
            F"Name of the restaurant is: {self.restaurant_name} and they serve {self.cuisine_type}!\n "
            F"I definitely recommend it!\n")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is Open from 5pm to midnight!\n")

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served
        if new_number_served >= self.number_served:
            print(f"Restaurant has served {self.number_served} customers!")
        else:
            print(f"ERROR!ERROR!")

    def increment_number_served(self, num_served):
        self.number_served += num_served
        print(f"Restaurant has served {self.number_served} customers!")


chinese = Restaurant("China Wok", "Chinese")
chinese.number_served = 11
chinese.set_number_served(12)
chinese.set_number_served(50)
chinese.increment_number_served(30)

"""9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0."""


class User:
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"User Personal Information:\n"
              f"First Name: {self.first_name}\n"
              f"Last Name: {self.last_name}")

    def greet_user(self):
        print(f"\nHello, {self.first_name} {self.last_name}! Welcome to our website!\n")

    def reset_Login_attempts(self, new_login_attempts):
        self.login_attempts += new_login_attempts
        self.login_attempts = 0
        if self.login_attempts == 0:
            print(f"Login attempts are reset: {self.login_attempts}!  \nYou can try to log in again!")
        else:
            (F"Password was incorrect! Try again!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        if self.login_attempts >= 1:
            print(F"You tried to log in {self.login_attempts} times!")
        else:
            print(f"Code is incorrect")


user1 = User("Maria", "Vilanova")
user2 = User("John", "Davos")
user3 = User("Daenerys", "Targarien")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user4 = User("Luka", "Aptsiauri")
user4.login_attempts = 1
user4.increment_login_attempts(1)
user4.reset_Login_attempts(2)

"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method."""


class Ice_Cream_Stand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type, number_served=0)

    flavors = ("Vanilla", "Chocolate", "Strawberry")

    def Ice_Cream_Flavors(self):
        print(f'{self.flavors} :This are all of the flavors what they have!')


summer = Ice_Cream_Stand("Italia", "Ice creams")
summer.Ice_Cream_Flavors()

"""9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    privileges = ("can add post", "can delete post", "can ban user")

    def show_privileges(self):
        print(f"Admin {self.first_name} {self.last_name} privileges include: {self.privileges}")


admin1 = Admin("Willy", "Wonka")
admin1.show_privileges()

"""9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges."""


class Privileges(Admin):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges=[]

    def show_privileges(self):
        super().show_privileges()


admin2 = Privileges(first_name="Salome", last_name="Aptsiauri")
admin2.show_privileges()

"""9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range."""

from class_practice.Classes_objects import Car
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
     """
   Initialize attributes of the parent class.
   Then initialize attributes specific to an electric car.
    """
     super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
