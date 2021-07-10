s = 'ABCDEFGHIJKLMNOAB'
print(s.find('A')) # Get the result of index 
print(s.find('z')) # As given substring not available its going to give you "-1"
print(s.find('A', 10,100)) # print the index within the boundary
print(s.find('A', 10,11)) # If given substring is not availabe then it going to print -1 result
print(s.rfind('B')) # its going to search backward direction, from right to left
print(s.index('D'))
