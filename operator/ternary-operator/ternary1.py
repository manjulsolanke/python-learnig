# Nesting is ternary operator is possible 
a = int(input('Enter the first number:',))
b = int(input('Enter the second number:',))
c = int(input('Enter the third number:',))
min = a if a < b and a < c else b if b < c else c 
print('Minimum value:', min)
max = a if a > b and a > c else b if b > c else c 
print('Maximum value:', max)