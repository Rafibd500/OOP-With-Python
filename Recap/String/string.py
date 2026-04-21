str = "Hello world!"
print(str[-1])

# string slicing
# substring = s[start : end : step]
print(str[-5:-1])
print(str[0:5:2])
print(str[::-1])
print(str[:5])
print(str[6:])
# str[0] = 'h' #string are immutable so we can't change it
mystr = "hello bhai"
del mystr
# print(mystr)

a = "             Hello         "
a = a.strip()
print(a)

st = "Python is good"
st.replace("Python", "Java")
print(st)

# concat string
x = "hello "
y = "world"
z = x*3
xy = x+y
print(xy)
print(z)

# String templete class ---------
# f-string → fastest & cleanest
# Template → safer, useful for external data
# format() → traditional method
print(f'{{Hello}}{{{{Hello}}}}')
nm = "Rafiqul Islam"
lang = "Python"
print('My name is {}. I love {}'.format(nm, lang))
# from string import Template
# str5 = Template("$hello, I am $name.")
# result = str5.safe_substitute(hello = x, name = nm)
# print(result)



# String Membership Testing
# in keyword checks if a particular substring is present in a string.
str10 = "Geeks for geeks"
print('ee' in str10) 
print('eee' in str10)