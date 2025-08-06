#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

# arr = [1,2,1,2,3,3,3,2,1,3,1,3,5,3]
a = 'aaaaabbbbccc'

my_counter = Counter(arr)  #Very powerfull method return the element as key and count of the element

# print(my_counter) #Counter({3: 6, 1: 4, 2: 3, 5: 1})

# print(my_counter.items())  #dict_items([(1, 4), (2, 3), (3, 6), (5, 1)])
# print(my_counter.keys()) # dict_keys([1, 2, 3, 5])
# print(my_counter.values()) # dict_values([4, 3, 6, 1])
# print(my_counter.most_common(1)) #[(3, 6)] three repeated 6 time, IN THE MOST_COMMON PASSED PARAMETER TELLS HOW MANY COMMON

# print(my_counter.most_common(2)) # [(3, 6), (1, 4)]

#IF YOU WANT ONLY THE MOST COMMON ELEMENT USE THIS
print(my_counter.most_common(1)[0][0]) # 3 THIS IS MOST COMMON
