# Stings: ordered, immutable , text representation

# my_string = "hello, World"

# slicing
# substring = my_string[1:7]
# substring = my_string[:5] start from begging
# substring = my_string[::2] takes every second char
# substring = my_string[::-1] #reverse the string
# print(substring)
# print(my_string.upper())
# print(my_string.lower())

# print(my_string.startswith('he'))
# print(my_string.endswith('rld'))

# print(my_string.find('o'))
# print(my_string.count('o'))

# print(my_string.replace('World', "Universe"))

# my_string = 'How,are,you,doing?'
# my_list = my_string.split(",")
# new_string = ' '.join(my_list)
# print(new_string)

# from timeit import default_timer as timer

# my_list = ['a'] * 600000

# #bad
# start = timer()
# my_string = ''
# for i in my_list:
#     my_string += i
# stop = timer()
# print(stop-start)

# #good
# start = timer()
# good_string = ''.join(my_list)

# stop = timer()
# print(stop-start)

# %, .format, f-strings

# VERY OLD METHOD
# var = 10.0909
# mystring = "the variable is %.2f" % var
# print(mystring)

# OLD METHOD
# var = 10.0909
# var2 = 76
# mystring = "the variable is {:.2f} and {}".format(var, var2)
# print(mystring)

# NEW F-STRINGS
var = 10.0909
var2 = 76
mystring = f"the variable is {var} and {var2}"
print(mystring)