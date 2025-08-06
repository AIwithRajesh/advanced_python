#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

# arr = [1,2,1,2,3,3,3,2,1,3,1,3,5,3]
# a = 'aaaaabbbbccc'

# my_counter = Counter(arr)  #Very powerfull method return the element as key and count of the element

# print(my_counter) #Counter({3: 6, 1: 4, 2: 3, 5: 1})

# print(my_counter.items())  #dict_items([(1, 4), (2, 3), (3, 6), (5, 1)])
# print(my_counter.keys()) # dict_keys([1, 2, 3, 5])
# print(my_counter.values()) # dict_values([4, 3, 6, 1])
# print(my_counter.most_common(1)) #[(3, 6)] three repeated 6 time, IN THE MOST_COMMON PASSED PARAMETER TELLS HOW MANY COMMON

# print(my_counter.most_common(2)) # [(3, 6), (1, 4)]

#IF YOU WANT ONLY THE MOST COMMON ELEMENT USE THIS
# print(my_counter.most_common(1)[0][0]) # 3 THIS IS MOST COMMON

# my_counter = Counter(a)
# print(my_counter)

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
# print(pt) #Point(x=1, y=-4)

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
#  Remembers the order of insertion
# print(ordered_dict) # OUTPUT: OrderedDict({'b': 2, 'c': 3, 'd': 4, 'a': 1}) 

# from collections import defaultdict

# d = defaultdict(dict) #THIS FUNCTION HAVE A DEFAULT VALUE IF VALUE NOT EXIST SO RETURN DEFAULT
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3

# print(d['c']) # OUTPUT: 3

# print(d['e']) # OUTPUT: 0  IF VALUE DOESN'T EXIST THEN RETURN 0 
# IF I FO WITH NORMAL DICT THEN IT'S GIVE KEYERROR
# di = {}
# di['a'] = 1
# print(di['b']) # KeyError: 'b'

from collections import deque  #A DOUBLE ENDED QUEUE FAST APPENDS AND POPS FROM BOTH SIDE
d = deque()

arr = [1,2,3]
for i in arr:
    d.append(i)

# d.appendleft(4)
# d.popleft()
# d.clear()
d.extend([4,5,6])
d.extendleft([-3,-2,-1,0])
print(d)
d.rotate(1) # Rotete to the right side
d.rotate(-2) # this will rotate to left right 2 time
print(d)