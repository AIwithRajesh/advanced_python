#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque, ChainMap
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
# print(d)
d.rotate(1) # Rotete to the right side
d.rotate(-2) # this will rotate to left side two time
# print(d)

from collections import ChainMap # combine multiple dictionaries into one view

# d1: dict[str, int] = {'a': 1, 'b': 2}
# d2: dict[str, int] = {'b': 3, 'c': 4}

# print(d1 | d2)

# cm = ChainMap({},d1, d2)
# # print(cm['b']) #OUTPUT 2, only refer to first dict
# cm['y'] = -1
# cm['x'] = 2

# print(cm)  #OUTPUT ChainMap({'y': -1, 'x': 2}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4})

# CHAINMAP USING CONSTRUCTOR

# names: list[str] = ['Bob', 'Sandra']
# cm: ChainMap[str, None] = ChainMap.fromkeys(names, None)

# print(cm) #OUTPUT: ChainMap({'Bob': None, 'Sandra': None})
# cm.update({'Luigi': None})
# print(cm) #OUTPUT: ChainMap({'Bob': None, 'Sandra': None, 'Luigi': None})

# default_setting: dict[str, str | bool] = {
#     'theme': 'light',
#     'language': 'English',
#     'notifications': True
# }

# user_preferences: dict[str, str | bool] = {
#     'theme': 'Dark',
#     'notifications': False
# }

# preferences: ChainMap[str, str | bool] = ChainMap(user_preferences, default_setting)

# print(preferences)


# d1: dict[str, int] = {'a': 1, 'b': 2}
# d2: dict[str, int] = {'b': 3, 'c': 4}

# cm: ChainMap[str, int] = ChainMap(d1, d2)

# cm.maps.append({'y': 5, 'z': 6}) # this will on index level
# print(cm) #OUTPUT: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'y': 5, 'z': 6})

# # cm.update({'y': 5, 'z': 6}) # this will update first dict
# # print(cm) #OUTPUT: ChainMap({'a': 1, 'b': 2, 'y': 5, 'z': 6}, {'b': 3, 'c': 4})

# # WE CAN UPDATE THE VALUE OF ANY DICT 
# cm.maps[1].update({'q': 20})
# print(cm) #OUTPUT: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4, 'q': 20}, {'y': 5, 'z': 6})

d1: dict[str, int] = {'a': 1, 'b': 2}
d2: dict[str, int] = {'b': 3, 'c': 4}
d3: dict[str, int] = {'d': 5, 'e': 6}

cm: ChainMap[str, int] = ChainMap(d1, d2, d3)
print(cm.parents) #OUTPUT ChainMap({'b': 3, 'c': 4}, {'d': 5, 'e': 6}) Everything is parents of first dict

cm = cm.new_child({'AA': 1, 'BB': 2}) # THIS WILL RETURN THE NEW CHAINMAP WITH ADDED NEW CHILD
print(cm) #OUTPUT ChainMap({'AA': 1, 'BB': 2}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6})