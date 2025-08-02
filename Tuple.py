# Tuple: ordered, immutable, allows duplicate elements
# mytuple = ("MAx",) # this will recognize as string you have to add , after that
# print(type(mytuple))

mytuple = tuple(["max", 28, "Boston"]) #we can create tuple using tuple built in function
# print(mytuple)

# IF you want access element
item = mytuple[0]
# print(item)

# mytuple[0] = "Low" # this is not possible because tuple is immutable

# for i in mytuple:
#     print(i)

# if "max" in mytuple:
#     print("yes")
# else:
#     print("no")

print(mytuple.index("max"))

mylist = list(mytuple)
print(mylist)

mytuple2 = tuple(mylist)
print(mytuple2)


# SLICING
a = ("a", "b", "c", "d", "e", "f",)
b = a[-2] #a[1:5] #a[-2]
print(b)

# UNPACK ELEMENTS 
new_tuple = "Rajesh",24, "Noida"
name, age, city = new_tuple

print(name, age, city)

numbers_tuple = (1,2,3,4,5)
i1, *i2, i3 = numbers_tuple

print(i1)
print(i3)
print(i2) #This will take middle remaing elements as array

import sys
my_list1 = [0,1,2,"hello",True]
my_tuple = (0,1,2,"hello",True)

print(sys.getsizeof(my_list1), "bytes")
print(sys.getsizeof(my_tuple), "bytes")
