
# UNPACKING ARGUMENTS
# def foo(a,b,c):
#     print(a, b,c)

# d = {'a': 1, 'e': 3, 'c': 4} #TypeError: foo() got an unexpected keyword argument 'e'
# d = {'a': 1, 'b': 3, 'c': 4}
# foo(**d)

# def func(a, b, *, d, e):
#     print(a, b)
#     print(d, e)
# keywords arguments name should be same as parameter
# func(1,3, d="rajesh", e=23)

def foo(a, b, *args, **kwargs):
    print(a, b) # 1 2
    print(args) # (3, 4, 5) tuple
    print(kwargs) # {'name': 'Rajesh', 'age': '24'} dictionary

foo(1,2,3,4,5, name="Rajesh", age="24")
