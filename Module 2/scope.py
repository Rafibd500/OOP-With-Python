# local variable 
balance = 1000

def func(item, price):
    # local variable
    # balance = 2000
    # you can access global variable without using the global keyword
    print(balance)
    # if you want to modify a global variable, you have to use the global keyword
    # global balance
    # balance -= price
    str = f'item: {item}, balace: {balance}'
    print(str)
func('apple', 200)