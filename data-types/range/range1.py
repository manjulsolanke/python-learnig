r = range(10)
print(type(r)) # which type it is ?
print(r)
for x in r: # print each and every value of the range
  print(x) # "begin to end - 1", its going to print 1 to 9

r = range(10,22)
# indexing 
print("please try Indexing")
print(r[0]) 
print(r[-1])
# Slicing 
r = r[1:5]
print("please try slicing")
print(r)