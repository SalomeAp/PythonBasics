print("Hello World!")

a = 64
b = a - 4
msg = "Hello, This is Salome"
name = "Lasha"
location = "Tbilisi,Georgia"

print(b)
print(msg)
print(name)

print("This is beautiful day" + "," + "\n\nI think we should go outside")
print("\n\n\n But why?This is only for today" + "," + "\n" + location.upper() + "\n\t" + msg.strip().lower().title())
num1 = 3
num2 = 5
print("addition:", num1 + num2)
print("subtraction", num1 - num2)
print("division:", num2 / num1)
print("multiplication:", num1 * num2)
print("exponent:", num2 ** num1)  #cube,square
print("floor division:", num2 // num1) #how many num1 fits in num2
print("nodulo:", 20 % num1) #if results returns 1 than it is odd value #if results returns 0 than it is even number

num3 = "678"
num4 = 54.98 # int converts and prints only integer when value is float
print("Addition:"+str(num1+num2)) # str turns intigers into string and it gives us chance to concatinate
print("addition:", num1 + int(num3)+ int(num4))

# variables can hold different values such as :"names, values, string, int, double, boolean expression(yes or no, true or false)

status = True

#string: concatenate,upper(), lower(), str(), \t , \n
#integers: int(), add, subtract, divide, multiply, exponent, floor division, modulo, odd, even, floats/doable,**(extract,//,%