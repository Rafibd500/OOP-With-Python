# print('Set')
number = [10,20, 40, 30, 40, 30, 50, 10, 20]
number_set = set(number)
number_set2 = {10, 20, 30, 10, 20, 30}
# print(number_set)
# print(len(number_set))
# if 20 in number_set:
#     print('20 exist')
# print(99 not in number_set)
# print(number_set.issubset(number_set2))  # number_set er sob element number_set2 te ache kina    number_set <= number_set2
# print(number_set.issuperset(number_set2)) # number_set2 er sob element number_set te ache kina  number_set >= number_set2

# print(number_set | number_set2) #Union
# print(number_set & number_set2) #Intersection
# #another way
# print(number_set.union(number_set2))
# print(number_set.intersection(number_set2))

# print(number_set-number_set2) # elements present in number_set but not in number_set2
# print(number_set.difference(number_set2))

#symmetric difference - elements jegulo jekono ektay ache
print(number_set.symmetric_difference(number_set2))
print(number_set2^number_set)

#copy
number_set3 = number_set
print(number_set3)

# another some operations
s = {10, 20, 30, 40}
t = {11, 20, 22, 33, 40}

# union update - return set s with elements added from t. 2 methods:
# s.update(t)  
# s |= t

#intersection update: return set s keeping only elements also found in t. 2 mehtods:
# s.intersection_update(t)
# s &= t

#difference update: 	return set s after removing elements found in t
# s.difference_update(t)
# s -= t

#symmetric difference update: return set s with elements from s or t but not both
# s.symmetric_difference_update(t)

print(s)

# s.add(9990)   # add x to the set
# s.remove(9990)  # remove x from the set. if element not exist then gives KeyEroor
# s.discard(110)     # removes x from set s if present
# s.pop() # remove and return an arbitrary element from s; raises KeyError if empty
s.clear()
print(s)