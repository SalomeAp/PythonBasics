person1 = {"name": "Darwin",
           'age': 60,
           'location': 'world'
           }
print(person1['name'])
for key in person1:
    print(f"looping through keys: {key}")

for key in person1.values():
    print(f"looping through keys: {key}")

for key,value in person1.items():
    print(f"looping through keys: {key}")
    print(f"looping through values: {value}")

person = { "first_name": "Shorena",
           "last_name": "Maisuradze",
           "age": 27,
           "city": "Tbilisi",
           "country":"Georgia"}