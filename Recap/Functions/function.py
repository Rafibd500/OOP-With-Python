# Types of Function Arguments
# 1/ default arguments -- a parameter that assumes a default value if a value is not provided in the function call
def fun(a, b = 10):
    print(a+b)

fun(20)
fun(20, 50)

# 2/ keyword argument -- values are passed by explicitly specifing parameter name, so no order needed
def fun2(a, b):
    print(f'fun2 = {a*b}')
fun2(a=10, b=20)
fun2(b=10, a=20)

# 3/ positional argument -- values are passed by maintaining order.
def fun3(a, b):
    print(f'fun3 = {a+b}')

fun3(1,2)

# 4/ arbitary argument -- it allow a function to accept variable number of input. using two special keyword
# ---- This is useful when you don’t know in advance how many values will be passed.
# a/ *args -- collects extra positional (non-keyword) arguments as a tuple.
# b/ **kwargs -- collects extra keyword arguments as a dictionary.
def fun3(*args, **kwargs):
    print("args: ")
    for arg in args:
        print(arg)

    print("Kwargs")
    # print(kwargs)
    # for key, val in kwargs.items():
        # print(key, "-", val)
    for item, val in kwargs.items():
        print(item, val)

fun3(1,2, hello = 10, gello = 30, hello = 20)

