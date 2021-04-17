a = 10
b = 20
if a > b: 
    print('a is greater than b')
else:
    print('b is greater than a ')


# Chaining of relational operator is possible. In the chaining, if all
# comparisons return True then only result is True. If atleast one 
# comparison returns False then the results is False

print(10<20)
print(10<20<30)
print(10<20<30<40)
print(10<20<30<40>50)