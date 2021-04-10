# Instead of creating 3 object, python will create only one object and give 3 refernce to that object.
# Its called object re-usability
a = 10
b = 10
c = 10
print(a, b, c)
print(id(a))
print(id(b))
print(id(c))

b = 10.101010
c = 10.101010
print( b is c )