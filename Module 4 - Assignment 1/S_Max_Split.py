s = input()
n = len(s)
last = 0
list = []
l=0
r=0
for i in range (0, n):
    if s[i] == 'L': l+=1
    elif(s[i] == 'R'): r+=1
    if(r==l):
        list.append(s[last:i+1])
        last = i+1
        r = 0
        l = 0
print(len(list))
for str in list:
    print(str)
