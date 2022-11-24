Guests = ['John Lennon', 'Plato', 'nietzsche']
print(Guests[-1].title() + "," + "\t" + 'I would like to invite you on dinner' + "\n Please, come by 8 o'clock")
print(Guests[0].title() + "," + "\t" + 'I would like to invite you on dinner' + "\n Please, come by 8 o'clock")
print(F"{Guests[1].title()} \t I would like to invite you on dinner \n Please, come by 8 o'clock")
Removed_Guest = Guests.pop(-1)
print(Guests[-1])
print(Removed_Guest)
print(f"{Removed_Guest} : Can't Make it Tonight")
Guests.append('Socrates')
print(F"{Guests[-1].title()} , \t I would like to invite you on dinner \n Please, come by 8 o'clock")
Guests.insert(0,'Kant')
print(Guests)
print(F"{Guests[0].title()} , \t I would like to invite you on dinner \n Please, come by 8 o'clock")

cars = ['bmw', 'honda','Lexus', 'Tesla']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
Sorted_Cars_Asc = sorted(cars)
print(Sorted_Cars_Asc)
Sorted_Cars_Desc = sorted(cars,reverse=True)
print(Sorted_Cars_Desc)
Sorted_Cars_Desc.reverse()
print(Sorted_Cars_Desc)


