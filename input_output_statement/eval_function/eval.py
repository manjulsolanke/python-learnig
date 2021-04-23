# this is typically type casting function and always going to return str type
x = input("Enter something:")
print(type(x))

# alternative to type casting 
x = eval(input('Enter something:'))
print(type(x))

# expression 
x = eval("100*70")
print(x,(type(x)))