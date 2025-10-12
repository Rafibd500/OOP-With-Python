# def display_name(**karg):
#     for key, val in karg.items():
#         print(f"{key}:{val}")

# display_name(Name = "Amir khan", Age = "45")


def add_numbers(*args):  # the tuple made with our all argument
    s = 0
    for num in args:
    	s+=num
    return s

print(add_numbers(2, 3))
print(add_numbers(1, 2, 3, 4, 5))

