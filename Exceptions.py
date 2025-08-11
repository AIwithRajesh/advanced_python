# Errors and Exceptions

x = -5

# if x < 0:
#     raise Exception('x should to be positive')

# assert (x>=0), 'x is not positive'

# try:
# a = 5/0 #ZeroDivisionError: division by zero

# try:
#     a = 5/1
#     b = a + '10'
# except ZeroDivisionError as e:
#     print('an error',e)
# except TypeError as e:
#     print('type error', e)
# else:
#     print('everything is fine')
# finally:
#     print('cleaning..')


# OWN error 
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError:
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 100:
        raise ValueTooSmallError('value is too small', x)

try:
    test_value(20)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)