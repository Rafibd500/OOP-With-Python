tc = int(input())
for i in range (0,tc):
    str1 = input()
    ln = len(str1)
    flag = 0
    for i in range(0, ln-2):
        if((str1[i] == '0' and str1[i+1] == '1' and str1[i+2] == '0') or (str1[i] == '1' and str1[i+1] == '0' and str1[i+2] == '1')):
            flag = 1
            break
    if(flag):
        print("Good")
    else:
        print("Bad")
