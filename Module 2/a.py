def display_name(**karg):
    for key, val in karg.items():
        print(f"{key}:{val}")

display_name(Name = "Amir khan", Age = "45")