x = 10
def fun():
    global x
    x = 20
    print(x)
fun()
print(x)


# nonlocal keyword -- used for nested function to outer function variable
def fun1():
    y = 100
    def fun2():
        nonlocal y
        y = 200
        print(y)
    fun2()
    print(y)
fun1()

# LEGB rule
# L - local -- oi function er vitor ache kina
# E - Enclosing -- parent function er vitor ache kina
# G - Global -- globally ache kina
# B - Builtin -- builtin ache kina
x = 'Global'
def outerFunc():
    x = 'Enclosing'
    def innerFunc():
        x = "Local"
        print("Inner x:", x)
    innerFunc()
    print("Outer x:", x)

outerFunc()
print("Global x:", x)