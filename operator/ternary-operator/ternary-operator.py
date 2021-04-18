# ~a # Unary oprator
# a + b # binary operator
# c = first_value if condition else second_value

a = 200
b = 20
c = 30 if a > b else 40
print(c)

a = int(input('Enter First number:'))
b = int(input('Enter Second number:'))
min = a if a < b else b
max = a if a > b else b
print('The minimum value:', min)
print('The maximum value:', max)


