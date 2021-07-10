# WAP to find the first  occurrence of sub string in a main string
# mainstring.find(substring, beginnig, ending)
mainstr = input('Enter main string: ')
substr = input('Enter sub string:  ')

# find position of sub in mainstr
# search from 0th to last characters in mainstr 
n = mainstr.find(substr, 0, len(mainstr))
if n == -1:
    print('Sub string not found')
else:
    print('sub string found at position: ', n+1)