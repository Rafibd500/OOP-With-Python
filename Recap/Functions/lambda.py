x = lambda a:a+20
print(x(10))

def func(n):
    return lambda x:x*n
myfunc = func(10)
print(myfunc(50))