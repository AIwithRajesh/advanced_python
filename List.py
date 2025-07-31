# LISTS: Ordered, mutable, allow duplicate values

list = ["Mango", "Banana", "Pineapple"]
# print(list)

# my_list = list()

my_list2 = [2, True, "apple", "apple"]

list.append("Lemon") #APPEND A ELEMENT IN THE LAST OF ARRAY
list.insert(1, "Bluebarry") #INSERT A ELEMENT USING INDEX
list.pop() #REMOVE LAST ELEMENT
list.remove("Bluebarry") #REMOVE A SPECIFIC ELEMENT
list.clear() #CLEAER ALL ELEMENTS
list.reverse() #REVERSE THE LIST

if "Banana" in list:
    print("Yes")
else:
    print("No")

MYNUMBERS = [9,6,4,2,1]
MYNUMBERS.sort() #SORT THE NUMBER. THIS WILL CHANGE ORIGINAL LIST

# NEW_LIST = sorted(MYNUMBERS) #NEW LIST WITHOUT CHANGING ORIGINAL
# print(list)

# newlist = [0] * 5 # YOU CAN FILL THE ARRAY WITH SAME NUMBER AS YOU WANT
# print(newlist)
# newlist2 = [1,2,3,4,5]

# combine_list = newlist + newlist2
# print(combine_list)

# SLICING
# new_list = [1,2,3,4,5,6,7,8,9]
# # a = new_list[::2] # EVERY SECOND ELEMENT IN ARRAY
# # a = new_list[1:5] #SLICE ARRAY FROM INDEX 1 TO 5

# a = new_list
# print(a)

# list_org = ["banana", "cherry", "apple"]
# list_cpy = list_org

# list_cpy.append("lemon") # THIS WILL UPDATE ORG ARRAY BECAUSE BOTH ARRAY REFER TO SAME MEMORY

# list_cpy = list_org.copy() # USING COPY METHOD AND USING LIST FUNCTION ALSO
# list_cpy = list(list_org) 
# list_cpy = list_org[:] # THIS WILL ALSO COPY THE ARRAY
# list_cpy.append("lemon") 
# print(list_cpy)
# print(list_org)

mylist = [1,2,3,4,5,6]
b = [i*i for i in mylist]

print(mylist)
print(b)