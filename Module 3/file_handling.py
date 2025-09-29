f = open("msg.txt", "w")
print(f)
f.write("Hello world")

f = open("msg.txt", "r")
print(f.read())


# another way:
with open('hello.txt', 'w') as file:
    file.write("Hello dunia!\n")
    file.write("Hi dunia")
with open('hello.txt', 'r') as file:
    print(file.read())