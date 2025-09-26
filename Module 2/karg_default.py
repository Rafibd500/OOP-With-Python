def full_name(first, last):
    return f'{first} {last}'
# print(full_name('Rafiqul', 'Islam'))
# print(full_name(last = 'Islam', first = 'Rafiqul'))

# key argument
# def f_name(**arg)
def identity(first, last, **addition):
    # print(addition['title'])
    print(addition)
    for key, val in addition.items():
        print(key, val)
identity('a', 'b', title = 'abc', desc = 'xyz')

# return multiple parameter
def multiple(a, b):
    sum = a+b
    mul = a*b
    div = a/b
    mod = a%b
    sub = a-b

    #return in tuple
    # return sum, mul, div, mod, sub

    # return in list
    return [sum, mul, div, mod, sub]
print(multiple(1,2))