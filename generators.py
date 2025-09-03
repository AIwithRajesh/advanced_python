import sys

# def mygenerator():
#     yield 4
#     yield 3
#     yield 2
#     yield 5


# res = mygenerator()

# value = next(res)
# print(value)

# print(sum(res))
# print(sorted(res))

# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(4)

# value = next(cd)
# print(value)

# funstion will take lots of memory becauase of array
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# generators are memory sufficient because this track current state instead of storing all elements
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

# print(sys.getsizeof(firstn(100)))
# print(sys.getsizeof(firstn_generator(100)))


# fibonacci using generator
# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a , b = b, a + b

# fb = fibonacci(100)
# value = next(fb)
# value = next(fb)
# print(value)

mygenerator = (i for i in range(100) if i % 2 ==0)
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(100) if i % 2 == 0]
print(sys.getsizeof(mylist))