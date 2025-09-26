# function
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
def sum(num1, num2):
    result = num1+num2
    return result

def update(a):
    b = a + 100
    print(b)

update(sum(a,b))
