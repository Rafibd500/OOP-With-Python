n = int(input())
list = list(map(int, input().split()))
mn = 10000000000000
for num in list:
    cnt = 0
    while(num%2 != 1):
        num/=2
        cnt+=1
    mn = min(mn,cnt)
print(mn)