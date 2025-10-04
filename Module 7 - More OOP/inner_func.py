def double_decker():
    print("Printing double decker bus")
    def inner_bus():
        print("Printing inner bus")
        return 100
    return inner_bus

# print(double_decker()())

def do_something(work):
    print(1)
    work()
    print(2)

def coding():
    print("I am coding")
do_something(coding)

def sleeping():
    print('sleeping and dreaming in python')

do_something(sleeping)