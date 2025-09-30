n = int(input())
list = list(map(int, input().split()))
disc = {}
for num in list:
    if(num in disc): disc[num]+=1
    else: disc[num] = 1
cnt = 0
# print(disc)
for key, val in disc.items():
    if(key > val) : cnt+=val
    elif(key<val) : cnt+=val-key
print(cnt)