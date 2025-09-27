# Array, list, collection are almost same things
# index =   0  1   2   3   4   5   6   7   8  
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# index =  -9  -8  -7  -6  -5  -4  -3  -2  -1 
print(numbers)
print(numbers[3])
print(numbers[-3])
# numbers[start:end]
print(numbers[2:6])
print(numbers[0:7])
print(numbers[-6:-2])

# numbers[start: end: step]
print(numbers[2:7:1])
print(numbers[2:7:3])
print(numbers[2:7:-1]) #empty: bcz 2 the -1 kore jete thakle kokhono 7 pawa jabe na
print(numbers[7:2:-2])
print(numbers[2:])
print(numbers[:6])
print(numbers[:]) # shortcut to copy a list
print(numbers[::-1]) #shortcut to reverse a list