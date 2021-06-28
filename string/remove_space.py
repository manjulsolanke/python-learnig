# WAP for removing the space in string
# this is problems statement
if 'Manjul '=='Manjul': # space could lead to wrong result
    print('Welcome')
else:
    print('Name is not found')
name = '   Manjul Solanke   '
fname = 'Manjul Solanke'
print(name.lstrip()) # remove space from left side
print(name.rstrip()) # remove spaces from right side
print(name.strip())

#if name == fname:
#    print('Welcome ' + name)
#else:
#    print('Oppps Name not found')
#    
