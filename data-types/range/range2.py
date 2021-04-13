# form 1, range(n)
r = range(10)
print("print form 1 range")
print(r) # range(0, 10)


# form 2 range(begin,end-1)
r = range(1,10)
print("print form 2 range")
for x in r:
    print(x)

# Form 3 example
r = range(1,21,2) # increment by 2
print("Print increment values by 2 ")
for x in r:
    print(x)

s = range(1,20,3) # increment by 3
print("Print increment values by 3 ")

for x in s:
   print(x)

a = range(20,1,-5)
print("Print decrement values by 5 ")
for x in a:
    print(x)


