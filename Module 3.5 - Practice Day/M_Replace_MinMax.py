x = int(input())
list = list(map(int, input().split()))
mx = max(list); mn = min(list)
for i in range (0, x):
    if(list[i] == mx): list[i] = mn
    elif(list[i] == mn): list[i] = mx
print(*list)
