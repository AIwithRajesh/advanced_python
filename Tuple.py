# Tuple: ordered, immutable, allows duplicate elements
# mytuple = ("MAx",) # this will recognize as string you have to add , after that
# print(type(mytuple))

mytuple = tuple(["max", 28, "Boston"]) #we can create tuple using tuple built in function
print(mytuple)

# IF you want access element
item = mytuple[0]
print(item)

mytuple[0] = "Low" # this is not possible because tuple is immutable

for i in mytuple:
    print(i)

if "max" in mytuple:
    print("yes")
else:
    print("no")