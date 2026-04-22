# Adding Elements into List
# Elements can be added to a list using the following methods:

# append(): Adds an element at the end of the list.
# extend(): Adds multiple elements to the end of the list.
# insert(): Adds an element at a specific position.
# clear(): removes all items.

list1 = [1,2,3,3,4,5,6,6]
list2 = ['a', 2, True, False, 2.23]

list2.append(2000)
list2.append(list1)
print(list2)

list2.extend([10, 20, 30])

list2.insert(2, 1000)
# list2.clear()
print(list2)


# Removing Elements from List
# Elements can be removed from a list using the following methods:

# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.

list2.remove(1000)
list2.pop()
list2.pop(0)
del list2[1]
print(list2)