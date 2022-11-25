print('Manjul'  + 'Solanke') #concatenation 

#print('Manjul' + 10 ) # TypeError: can only concatenate str (not "int") to str
print('Manjul'+ '10')
print('Manjul' * 2) # String repitation operator
print( 2 * 'Manjul') # order is not important

#print('Manjul' * 'Manjul') # TypeError: can't mu

#print('Manjul' * '3') #TypeError: can't multiply sequence by non-int of type 'str'
print ('#' * 10 + ' String Multiplication ' + '#' * 10)
name = 'manjul'  
print(name * 3)

print ('#' * 10 + ' number to string multiplication ' + '#' * 10)
print (5 * name)

print('Manjul' * int('3')) # will work fine 