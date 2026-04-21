tc = int(input())
for i in range (0,tc):
    s1, s2 = input().split()
    s3 = ''
    ln1 = len(s1)
    ln2 = len(s2)
    if(ln1>ln2):
        for i in range(0, ln2):
            s3+=s1[i]
            s3+=s2[i]
        s3+=s1[ln2:]
    else:
        for i in range(0, ln1):
            s3+=s1[i]
            s3+=s2[i]
        s3+=s2[ln1:]
    print(s3)
