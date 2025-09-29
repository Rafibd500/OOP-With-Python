print("Hello world")
num = (10, 20 , 30, 'Hello world')
# print(type(num))
# print(num)
# print(num[1:3])
# print(num[:-1])

# Tuples are immutable:
# num[1] = 200 # give error

mix = (10, 20, 30, ['karim', 'rahim', 'Kashem'], (100, 200, 300), 'Rakib', ['alu', 20, 'kodu'])
print(mix)
print(mix[3])
print(mix[3][2])
# tuple er vitor kono mutable data thakle deta abar change kora jabe:
mix[3][2] = 'Bashem'
print(mix[3][2])


# give error: karon tuple er vitor tuple er data change korte chacchi. jeta immutable 
# print(mix[4][1])
# mix[4][1] = 999


# length of tuple 
print(len(mix))

if('Rakib' in mix):
    print('exist')

for item in mix:
    print(item)