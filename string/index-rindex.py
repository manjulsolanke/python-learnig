S = 'ABCDEFGHIJKABCD'
print(S.index('B'))
#print(s.index('T')) # if given string is not availabel then its going to throw ValueError unlike find and rfind -1
print(S.index('E', 2, 5))
print(S.index('K')) # right to left
#print(S.index('Z')) # String is not availabel so we are going to get "ValueError: substring not found"
print(S.index('C', 0, 1000))
print(S.rindex('K'))
print(S.rindex('G', 5, 8)) # right to left

