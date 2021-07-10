FName = input('Enter the first string:')
LName = input('Enter the second string:')
if FName == LName:
    print('Both the string are equal')
elif FName < LName:
    print (FName, 'is less than', LName)
else:
    print(FName, 'is greater than or equal to', LName)
    