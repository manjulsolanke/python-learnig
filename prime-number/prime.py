n = int(input('Enter any number:'))
if n <= 1:
    print('it is not prime number:')
else:
    is_prime=True
    for x in range(2,n):
        if n%x == 0:
            is_prime=False
            break
    if is_prime==True:
        print('It is prime number')
    else:
        print('It is not prime number')
