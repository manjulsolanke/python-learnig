
print(10 == 20)
print(10 != 20)
print(1 == True)
print( 'foo' == 'foo')
print("\n")

a = 10
b = 10.0
print(a is b) # Reference/address comparison
print(a == b) # content reference 

print("\n")
a = 10
b = 10
print(a is b) # Reference/address comparison
print(a == b) # content reference 
print("\n")
l1 = [10, 20, 30]
l2 = [10, 20, 30]
print(l1 is l2) # Reference/address is not same, hence False 
print(l1 == l2 ) # Content is same hence True
l3 = l1
print( l1 is l3) # now l1 and l2 reference to same object hence True
