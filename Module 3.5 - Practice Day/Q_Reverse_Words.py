list = list(map(str, input().split()))
n = len(list)
x = 0
for st in list:
    x+=1
    if(x == n): print(st[::-1], end = "")
    else : print(st[::-1], end = " ")