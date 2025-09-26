def sum(a, b, c=40):
    return a+b+c
s = sum(5, 10, 20)
print(s)

def sm(a, b, *numbers):
    print(numbers)
    s = 0
    for n in numbers:
        s+=n
    return s
res = sm(10,20,30, 40, 50)
print(res)