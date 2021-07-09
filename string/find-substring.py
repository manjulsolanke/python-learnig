s = 'ABCDEFGHIJKLMNOAB'
print(s.index('D'))
print(s.find('A'))
print(s.find('z')) # As given substring not available its going to give you "-1"
print(s.rfind('B')) # its going to search backward direction, from right to left
print(s.find('A', 10,100)) # print the index within the boundary
