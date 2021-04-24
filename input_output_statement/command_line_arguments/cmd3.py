# In command line argument is avaialbe only in string format
from sys import argv
print(argv[1]+argv[2]) # String format 
print(int(argv[1])+int(argv[2])) # type casting