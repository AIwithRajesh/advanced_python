# itertools: product, permutations, accumulate, groupby, and infinite iterators

from itertools import product
# Product returs the all possible combinations (including repeated number) of givem items in iterables 
a: list[int] = [1,2]
b: list[int] = [3]

# prod = product(a,b, repeat=2) 
# print(list(prod))  #OUTPUT: [(1, 3), (1, 4), (2, 3), (2, 4)]

# # REAL WORLD USE CASE

# cloth_color: list[str] = ['Red', 'Blue']
# size: list[str] = ['M', "S"]

# for combo in product(cloth_color, size):
#     print(combo) # OUTPUT ('Red', 'M')
#                         # ('Red', 'S')
#                         # ('Blue', 'M')
#                         # ('Blue', 'S')

# # # BRUTE FORCE PROBLEM
# # for code in product('0123456789', repeat=4 ):
# #     print(''.join(code))

from itertools import permutations
# # RETURNS ALL POSSIBLES ORDERINGS OF GIVEN INPUTS IN THIS ORDER MATTERS

# a: list[str] = [1,2,3]
# perm = permutations(a)

# # print(list(perm)) #OUTPUT: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# perm = permutations(a, 2) # Give can give as second parameter as length
# print(list(perm)) #OUTPUT: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import combinations, combinations_with_replacement
arr: list[int] = [1,2,3,4]

com: combinations = combinations(arr, 2)
# RETURNS COMBINATIONS OF GIVEN INPUTS WITH NOT REPETED COMBINATIONS AND ORDER DOESN'T MATTER

# print(list(com)) #OUTPUT: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

ice_cream: list[str] = ['Vanilla', "Strawberry", "Chocolate"]

com_wr = combinations_with_replacement(ice_cream, 2)
# ALL THE COMBINATIONS WITH REPEAT VALUES
# print(list(com_wr))
#OUTPUT: [
#     ('Vanilla', 'Vanilla'),
#     ('Vanilla', 'Strawberry'),
#     ('Vanilla', 'Chocolate'),
#     ('Strawberry', 'Strawberry'), 
#     ('Strawberry', 'Chocolate'),
#     ('Chocolate', 'Chocolate')
# ]

# from itertools import accumulate
# import operator
# savings: list[int] = [1,2,5,3,4]

# # acc: accumulate = accumulate(savings, func=operator.mul) #OUTPUT: [1, 2, 10, 30, 120]
# acc: accumulate = accumulate(savings, func=max) #OUTPUT: [1, 2, 5, 5, 5]

# print(list(acc))


from itertools import groupby
# a: list[int] = [1,2,3,4]

# def smaller_then_3(x):
#     return x < 3

# group_obj: groupby = groupby(a, key=lambda x: x < 3)
# for key, value in group_obj:
#     print(key, list(value))

persons: list[object] = [
    {'name': 'Tim', 'age': 25},
    {'name': 'Lisa', 'age': 25},
    {'name': 'Lisa', 'age': 27},
    {'name': 'Claire', 'age': 28}
]

group_obj: groupby = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))


from itertools import count , cycle, repeat

# for i in count(10):
#     if i == 20:
#         break
#     print(i)

a = [1,2,3]
# for i in cycle(a): # Infinite cycle after printing 1,2,3 and so
#     print(i)

for i in repeat(a, 4): #it's repeat 4 times 
    print(i)