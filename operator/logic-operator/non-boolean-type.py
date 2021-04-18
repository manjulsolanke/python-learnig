# "and" Operator
# 0 means False, non zero is True
# Empty string, list, set, tuple, dict always "False"
x = 10
y = 20
a = 0
print( x and y) # X evaluated True as its not empty so y is answer
print( a and y ) # a evaluated False as its empty hence a is aswer
print("\n")

# or operator
print(x or y) # if x true, result is always true, if x is false need to check on y
print( a or y)
print("\n")

# not operator
# 0 is false 
# 1 is true 
# Result always in boolean
a = 'foo'
b = ''
print(not a) # a is not empty mean False # Not true means False
print(not b) # b is  empty True  # Not false mean True 
print( not 0) # not false means true
print(not 10) # not true means false