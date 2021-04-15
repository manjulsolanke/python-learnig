def f1():
    return 10
x = f1()
print(x)

def f2():
    print("Hello")
x = f2()
print(x)
    

# PVM will  create only one object for all the none reference 
a = None
b = None
c = None
d = None
print("All object should return the same value")
print(a,b,c,d)
print(id(a), id(b), id(c), id(d)) # we will get same value
