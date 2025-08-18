import random 

# sudo random they are reproducable
# generates betwween 0 to 1 floating number
# a = random.random()

# this will generates a floating value between two given number
# b = random.uniform(1,10)
# print(b)

# if you want to generate integer values use
# c = random.randint(20,100)
# this will never include end number
r = random.randrange(1,10)
# print(r)

# In this 0 is mean and 1 is standard deviation tells how spread out are from the mean
a = random.normalvariate(0,1)
# print(a)

myList = list("ABCDEFGH")
# Pic random from iterator using random.choice
# choice = random.choice(myList)

# pics random unique elements
# sample = random.sample(myList, 3)
# print(sample)

# random.shuffle(myList)

# print(myList)

# random.seed(1)
# print(random.random())
# print(random.randint(1,10))

# random.seed(2)
# print(random.random())
# print(random.randint(1,10))

# random.seed(1)
# print(random.random())
# print(random.randint(1,10))

# random.seed(2)
# print(random.random())
# print(random.randint(1,10))

# This is very useful in passwords, tokens, API keys, OTP, Secure session IDs
# this is slower than random
import secrets

# genrerates btw 0 to 9 , 10 will be exclude
# a = secrets.randbelow(10)
# print(a)

# generates bits numbers btw 0 to 15
# b = secrets.randbits(4) 
# print(b)

# a = secrets.choice(myList)
# print(a)

# Very useful when working with large number of datasets
# written in C, optimized for arrays
# Can generates millions of random numbers very fast 
import numpy as np

# this will generate a list with three floating values
# we can add dimensions like (3,3) first is the count of elements should be
# second parameter will be array dimension
a = np.random.rand(3,3)
# [[0.07282441 0.17687065 0.48203544]
#  [0.12061702 0.63211847 0.85710731]
#  [0.25307534 0.1903152  0.93717029]]
# print(a)

# randint = np.random.randint(0,10)
# we can extand array adding dimension 
# randint = np.random.randint(0,10, (3,4))
# print(randint)
# [[5 0 0 9]
#  [9 0 1 4]
#  [8 7 0 8]]
# arr = np.array([[5, 0, 0, 9], [9, 0, 1, 4], [8, 7, 0, 8]])
# np.random.shuffle(arr)

# print(arr)
np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))