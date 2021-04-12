l = [10, 20, 50, 'manjul', 40, 10 ] # Duplicates are allowed, order is imp.
print(type(l)) # which type it is?
print(l)
print(l[5]) # print the 5th index
print(l[-1]) # indexing
print(l[1:4]) # slice operator

# Append and remove in list

l=[] # Created a empty list
l.append(66) # Append
l.append(77)
print(l)
l.remove(66) # remove the object
print(l)

# Object can be changed/replaced hence it called List is muteable.

l=[11,22,33,44,55,66]
print("Before change")
print(l)

l[0]=77
print("After change")
print(l)
