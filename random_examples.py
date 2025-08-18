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

random.shuffle(myList)

print(myList)