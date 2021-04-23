from  sys import argv
args = argv[1:]
sum = 0
for x in args:
   # sum = sum + x # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    sum = sum + int(x) # should work
    #sum = sum + eval(x)# should work
print('the sum:', sum) 

#print(input('Enter the number'))