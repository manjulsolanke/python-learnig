s = {10,20,30,40}
print(type(s)) # which type it is?
print(s)
s = {10,20,30, 'manjul',40,10,20,30} # Duplicat boject is there, but it won't print duplicate object.
print(s)

# imp comments

#print(s[0]) # orders is not there so indexing not possible. we can get type errors
#print(s[1:3]) # slicing is not possible as it doesn't support indexing



# Adding object in set is possible.

s = {10,20,30,40,'Manjul',50}
print("Before add ")
print(s)
s.add(55) # added 55 in set
print("After add")
print(s)

# this is create dict data type not empty set.
s = {}
print(type(s))


# Create a empty set git s
s = set()
print(type(s))
