n, k = map(int, input().split())
list = list(map(int, input().split()))
preSum = [list[0]]
for i in range(1, n):
    x = preSum[i-1] + list[i]
    preSum.append(x)
    
# print(*preSum)
while(k):
    a, b = map(int, input().split())
    if a==1: print(preSum[b-1])
    else: print(preSum[b-1]-preSum[a-2])
    k-=1