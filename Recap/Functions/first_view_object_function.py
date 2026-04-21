# In Python, functions are treated as first-class objects. This means they can be used just like numbers, strings, or any other variable. You can:

# 1/ Assign functions to variables.
# 2/ Pass them as arguments to other functions.
# 3/ Return them from functions.
# 4/ Store them in data structures such as lists or dictionaries.
# 1/
def hello(x):
    return f'hello world {x}'

xyz = hello
print(xyz("Python"))

# 2/
def func(f, x):
    return f(x)

print(func(hello, "Java"))

# 3/
def func3():
    def func2():
        return f"Inner function"
    return func2
fun = func3()
print(fun())

# 4/
list = [hello, func3]
y = list[0]
print(list[0]("rust"))
print(y("c/c++"))

# store in dictionary
def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
dict = {
    'add_num' : add, 
    'subtract_num' : subtract
}
print(dict["add_num"](4, 10))
a = dict['subtract_num']
print(a(20, 10))