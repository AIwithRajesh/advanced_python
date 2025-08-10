# Lambda Arguments: Expression
# IT use when needs smaller function for just once
# Higher order function

add10: int = lambda x: x + 10

print(add10(5)) #OUTPUT: 15

mult: int = lambda x,y: x*y
print(mult(2, 10)) #OUTPUT: 20

points2D = [(1,2), (15,1), (5, -1),(10, 4)]

# points2D_sorted = sorted(points2D) #bydefault its sort using x values
# print(points2D_sorted)  #OUTPUT: [(1, 2), (5, -1), (10, 4), (15, 1)]

# example def 
def sort_by_y(x):
    return x[1]

# points2D_sorted = sorted(points2D, key=lambda x: x[1])
# points2D_sorted = sorted(points2D, key=sort_by_y)
# print(points2D_sorted) #OUTPUT: [(5, -1), (15, 1), (1, 2), (10, 4)]

# map(func, seq)
# a: list[int] = [1,2,3,4,5]
# b: object = map(lambda x: x*2, a)

# print(list(b)) #OUTPUT: [2, 4, 6, 8, 10]

# c = [x*2 for x in a] #This is very easy and recommended 
# print(c) #OUTPUT: [2, 4, 6, 8, 10]

#filter(func, seq)
a: list[int] = [1,2,3,4]

# b = filter(lambda x: x%2==0, a)
# print(list(b)) #OUTPUT: [2, 4, 6]
# c = [x for x in a if x %2 == 0]
# print(c) #OUTPUT: [2, 4, 6]

# reduce(func, seq)
from functools import reduce

product_a = reduce(lambda x,y: x*y, a)
print(product_a) #OUTPUT 24
