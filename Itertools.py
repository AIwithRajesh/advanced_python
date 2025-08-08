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

from itertools import accumulate

savings: list[int] = [100, 200, 300, 400]

acc: accumulate = accumulate(savings)

print(list(acc))
