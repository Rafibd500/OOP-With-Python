print('Lambda')
# def doubled(num):
#     return num*2
# print(doubled(5))

doubled = lambda num: num*2
squared = lambda num: num*num
print(doubled(15))
print(squared(5))

addition = lambda a, b: a+b
print(addition(2,5))

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
doubled_num = map(doubled, numbers)
suqared_num = map(lambda x:x*x, numbers)
print(list(doubled_num))
print(list(suqared_num))


persons = [
    {
        "name": "karim", "age": 20, "location": "dhaka" 
    },
    {
        "name": "rahim", "age": 30, "location": "mirpur" 
    },
    {
        "name": "kuddus", "age": 40, "location": "barishal" 
    }
]
filtered = filter(lambda person: person["age"]>=30 , persons)
print(list(filtered))