# decorators function based and class based
import functools
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a"
)

def start_end_decorators(func):

    @functools.wraps(func)
    def wrapper(*args, **kwards):
        print('start')
        res = func(*args, **kwards)
        
        print('end')
        return res
    
    return wrapper


# def print_name():
#     print("Alex")

# start_end_decorators(print_name)

# @start_end_decorators
# def print_name():
#     print("Alex")

# @start_end_decorators
# def addition(x, y):
#     return x + y

# print(help(addition))
# print(addition.__name__)

def log_decorators(func):

    def wrapper(*args, **kwards):
        logging.info(f"calling {func.__name__} args={args},kwards={kwards}")
        res = func(*args, **kwards)
        return res

    return wrapper
    
@log_decorators
def addition(x, y):
    return x + y

res = addition(13, 190098)
# print(res)


# def repeat(num_times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwards):
#             for _ in range(num_times):
#                 res = func(*args, **kwards)
#             return res
#         return wrapper
#     return decorator

# @repeat(num_times=3)
# @start_end_decorators
# def greet(name):
#     print(f'Hello, {name}')

# greet("Alex")


class countClass:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwards):
        self.num_calls += 1
        print(f'THis is executed {self.num_calls}')
        return self.func(*args, **kwards)

@countClass
def greet():
    print("alex")

greet()
greet()