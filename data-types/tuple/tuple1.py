t=(10,20,30,'Manjul')
print(type(t))
print(t)
print(t[1]) # indexing
print(t[-1]) # indexing
print(t[1:3]) # slice

#t[0] = 77 # Type error, since tuple doesn't support the change/replace.

k = (10) # without comma, PVM will consider as int data type.
print(type(k))

j = (10,) # with comma, PVM will consider this as tuple data type. 
print(type(j))
