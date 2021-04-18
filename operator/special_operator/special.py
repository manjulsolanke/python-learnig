a = 10
b = 10
print( a is b )
print( a is not b )
a = 'foo'
b = 'foo'
print( a is b) # string
print( a is not b) 

l1 = [10,20,30]
l2 = [10,20,30]
print(id(l1))
print(id(l2))
print( l1 is l2)
print( l1 is not l2)