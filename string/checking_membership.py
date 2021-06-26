# To kknow whether sub string is in main string or not
str  = input('Enter the string ') # space given at the end of the line 
subStr = input('Enter the sub string ')


if subStr in str:
    print(str+  ' is found in main string ')
else:
    print(subStr+  ' is not found in the main string ')