l = [10,20,30,40]
b = bytearray(l)
print("What type of datatypes it is?")
print(type(b))
print("print the objects")
print(type(l))
print("print the indexing")
print(b[0])
print("print the indexing")
print(b[-1])
print("print the slicing")
print(b[1:3])

# muteable 
b[0] = 77
for x in b:
    print(x)