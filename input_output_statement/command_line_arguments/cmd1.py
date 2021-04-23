from sys import argv
print("The number of command line arguments:", len(argv))
print('The list of command line arguments:', argv)
print('The commmand line arguments one by one:')
for x in argv:
    print(x)
