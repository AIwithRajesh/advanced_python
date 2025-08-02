# Dictonary: Key-Value pairs, Unordered, Mutable
mydict = {
    "name": "Henry",
    "age": 30,
    "city": "New York"
}

mydict["email"] = "abc@gmail.com" # ADD KEY VALUE
value = mydict["email"]
# print(value)

# del mydict["email"]
# # mydict.pop("age")
# mydict.popitem()
# print(mydict)

# mydict1 = dict(
#     name="Henry",
#     age=30,
#     city="New York"
# ) #You don't need colon in dict function

# print(mydict1)

# if "name" in mydict:
#     print(mydict)
# else:
#     print("Nothing")

# try:
#     print(mydict["name"])
# except:
#     print("Something Wrong")

# for key in mydict: # THis will extract keys
#     print(key)

# for key in mydict.keys(): # THis will extract keys
#     print(key)

# for value in mydict.values(): # THis will extract keys
#     print(value)

# mydict_cpy = mydict
# mydict_cpy = mydict.copy() # This will create saperate memory not refer to same 
# mydict_cpy = dict(mydict) # This will create saperate memory not refer to same 

# mydict_cpy["email"] = "xyz@gmail.com" # This will modify original dict also because refer to same memory
# print(mydict_cpy)
# print(mydict)

# my_dict2 = {
#     "name": "Henry",
#     "age": 30,
#     "city": "New York"
# }

# my_dict3 = dict(name="Mary", age=23, email="abc@gmail.com", city="New York")

# my_dict2.update(my_dict3)

# print(my_dict2)

dict_number = {3:9, 6:36, 9:81}

for key in dict_number:
    print(key)

# We can use tuple as key but List can't use as key because list mutable and not hashable
mytuple = (8,9)
mydict4 = {mytuple: 17}

print(mydict4)