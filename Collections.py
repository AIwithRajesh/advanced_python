#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

arr = [1,2,1,2,3,3,3,2,1,3,1,3,5,3]

my_counter = Counter(arr)  #Very powerfull method return the element as key and count of the element

print(my_counter) #Counter({3: 6, 1: 4, 2: 3, 5: 1})