# object is same, so we should get same value
x = 10
y = x
print(x,y)
print(id(x))
print(id(y))

# Now value of "Y" would be different
y = x + 1
print(y)
print(id(y))
