n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)
mn = min(arr)
for i in range(0, n):
    if arr[i] == mx:
        pos = i
    if(arr[i] == mn):
        pos2 = i
arr[pos2] = mx
arr[pos] = mn
print(*arr)