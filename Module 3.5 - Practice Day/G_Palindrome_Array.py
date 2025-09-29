x = int(input())
st = list(map(int, input().split()))
st2 = st[::-1]
if(st == st2):
    print("YES")
else:
    print("NO")