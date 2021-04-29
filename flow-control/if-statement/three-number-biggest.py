print(10 * '#' )
a = int(input('Ether the 1st number:',))
b = int(input('Ether the 2nd number:',))
c = int(input('Ether the 3rd number:',))

if a > b and a > c:
    print('Biggest number:', a)
elif b > c:
    print('Biggest number:', b )
else:
    print('biggest number is c:', c)


print(10 * '#')
a = int(input('Ether the 1st number:',))
b = int(input('Ether the 2nd number:',))
c = int(input('Ether the 3rd number:',))

if a < b and a < c:
    print('Smallest number:', a)
elif b < c:
    print('Smallest number:', b )
else:
    print('Smallest number is c:', c)    
print(10 * '#' )