#Set: unordered, mutable, no duplicates

# myset = {1,2,3}
# myset = set([1,2,3,4]) #THis will also create set
# print(myset)

# myset = set("hello")
# print(myset) {'l', 'h', 'o', 'e'}

# myset = set()
# myset.add(1)
# myset.add(2)
# myset.add(3)

# # myset.discard(1)
# # myset.remove(2)

# print(myset.pop()) # remove first element

# print(myset)

# odds = {1,3,5,7,9}
# evens = {0,2,4,6,8}
# prime = {2,3,5,7}

# u = odds.union(evens) #combine two sets

# # i = odds.intersection(evens) #set() empty result because both don't have same numbers

# i = odds.intersection(prime) 

# print(i) #{3, 5, 7} have this common numbers

# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# diff = setA.difference(setB) 
# print(diff) # {4, 5, 6, 7, 8, 9} retuen diff elements which not in given set

# diff1 = setB.difference(setA)
# print(diff1) # {10, 11, 12} 

# diff = setA.symmetric_difference(setB)
# print(diff) # {4, 5, 6, 7, 8, 9, 10, 11, 12} this will return different elememts from both set

# setA.intersection_update(setB)
# print(setA) # {1, 2, 3} update the set with same values other will bw removed

# setA.difference_update(setB)
# print(setA) # {4, 5, 6, 7, 8, 9} remove the common elements from given set

# setA.symmetric_difference_update(setB)
# print(setA) #4, 5, 6, 7, 8, 9, 10, 11, 12} update the different elements from both set


# setA = {1, 2, 3, 4, 5, 6}
# setB = {1, 2, 3}
# setC = {7,8}
# print(setA.issubset(setB)) False because setB doesn't have all elements of setA
# print(setB.issubset(setA)) True because setA have all elements of the setB

# print(setA.issuperset(setB)) True because setA contains all the elements of setB 
# print(setB.issuperset(setA)) False because SetB doesn't contains 4,5,6 

# print(setA.isdisjoint(setB)) False becuase both contains some same values
# print(setA.isdisjoint(setC)) True because contains different elements/


# setA = {1, 2, 3, 4, 5, 6}
# setB = setA

# setB.add(7)
# print(setB) {1, 2, 3, 4, 5, 6, 7}  this simple assignment both point to the same set
# print(setA) {1, 2, 3, 4, 5, 6, 7}

# setA = {1, 2, 3, 4, 5, 6}
# # setB = setA.copy()
# setB = set(setA)  #both copy and set method will work

# setB.add(7)
# print(setB)  {1, 2, 3, 4, 5, 6, 7}
# print(setA)  {1, 2, 3, 4, 5, 6}


#  FROZENSET: IMMUTABLE
a = frozenset([1,2,3,4])
print(a) #frozenset({1, 2, 3, 4})

a.add(1) #this will give error 
a.remove(1) #this will give error 
