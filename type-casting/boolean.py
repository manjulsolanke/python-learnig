# Converting from int to boolean
# Non zero always True and only zero is false value
a = bool(10)
print(a)

b = bool(0)
print(b)

a = bool(-20)
print(a)

a = bool(+10)
print(a)

# Converting from float to boolean

a = bool(0.0)
print(a)

a = bool(0.1) # non zero always true
print(a)

# Converting from complex to boolean
a = bool(0 + 0j)
print(a)
a = bool(0 + 0.001j)
print(a)


# Converting from str to boolean

a = bool('True')
print(a)

a = bool('False')
print(a)

a = bool('Yes')
print(a)

a = bool('') # only empty string goning to print false
print(a)

