def isPal(str):
    str2 = str[::-1]
    if(str == str2):
        return True
    else:
        return False
str = input()
str2 = int(str[::-1])
print(str2)
if(isPal(str)):
    print("YES")
else:
    print("NO")
