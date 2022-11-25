print( '*' * 10 + " Defined the dict and print ", '*' * 10)
d = {1:'a', 2:'b', 3: 'c', 4:'d'}
print(d[1], d[2])

print( '*' * 10 + " print keys and values ", '*' * 10)
print(d.keys())
print(d.values())

print( '*' * 10 + " change the kay value ", '*' * 10)

d[1] = 'z'
print(d)

print( '*' * 10 + " delete key value ", '*' * 10)
del d[2]
print(d)