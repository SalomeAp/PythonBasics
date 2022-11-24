# chapter9  Working with classes and instances
# hiding from the object  - encapsulation - child classes
# OOPs concepts - class, object, encapsulation
"""class Car:
    # attribute - required, optional(default)
    def __init__(self, make, model, year, battery):
        self.make = make
        self.model = model
        self.year = year
        self.__mileage = 0
        self.battery = battery
    # behaviour - actions i need to do,
    # CRUD -> set, get,other
    def get_description(self):
      Gets details of the car
        print(F"name: {self.make}, model: {self.model}, "
              F"year: {self.year}, mileage: {self.__mileage}")

    def set_mileage(self, new_mileage):
        sets the mileage not less than current mileage
        if new_mileage > self.__mileage:
            self.__mileage = new_mileage
        else:
            print("mileage was less than current mileage, cannot be done")

    def add_to_mileage(self, miles):
        increments the mileage with given miles
        if miles >0:
           self.__mileage = self.__mileage + miles
           print(f"{miles} miles were added to your car mileage")
        else:
            print()"""

"""car1 = Car("bmw", "X5", 2022)
print(car1.make, car1.year + 1, car1.model)
car1.get_description()
car1.model = "X5 M"
car1.set_mileage = 60
car1.get_description()
car1.set_mileage = 10
car1.get_description()
car1.add_to_mileage(100)
car1.get_description()"""


class Car():


      def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
       self.odometer_reading = 0

      def get_descriptive_name(self):

      long_name: str = f"{self.year}{self.make}{self.model}"
      return long_name.title()

      def read_odometer(self):
      print("This car has " + str(self.odometer_reading) + " miles on it.")

      def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
        else:
           print("You can't roll back an odometer!")

      def increment_odometer(self, miles):
      self.odometer_reading += miles
