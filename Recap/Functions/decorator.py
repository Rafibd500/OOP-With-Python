def changecase(func):
    def inner():
        return func().upper()
    return inner
@changecase
def hello():
    return 'Hello world'
# x = hello()
print(hello())