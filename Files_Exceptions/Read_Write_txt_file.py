# chapter 10:

with open("../Data/products.txt.txt") as prod_list:
    contents = prod_list.read()
    print("contents of the file: \n", contents)

with open("../Data/products.txt.txt") as prod_list:
    all_lines = prod_list.readline()
    print(all_lines)
    print("now we are trying to loop through the content")

for line in all_lines:
    print(line)

print("___________Write File_________")


with open("../Data/products.txt.txt", 'w') as prod_list:
    prod_list.write("cheese\n")
    prod_list.write("bread\n")
    prod_list.write("milk\n")
    new_data = prod_list.readline()


for line in new_data:
    print(line)
