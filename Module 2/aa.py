# def add_num(*nums):     # the tuple made with our all argument
#     s = 0
#     for num in nums:    # take number with for loop from our tuple
#         s += num        # add the tuple elements
#     return s


# print(add_num(10, 20))    # ans: 30
# print(add_num(10, 20, 30, 40, 50)) # ans: 150

def person(**kwargs):   # the value pair tuple made with our all key vakye argument
    for key, value in kwargs.items():   # for loop to extract the pairs from tuple
        print(f"{key} : {value}")       # print the key and values

person(name="Rafi", age=22, city="Dhaka")