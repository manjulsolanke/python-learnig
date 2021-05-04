print(5 * '#', 'WAP to display sum of first n numbers', 5 * '#')
n=int(input('Enter the number:'))
sum = 0
i = 1
while i<=n:
    sum=sum+i 
    i=i+1
print('The sum:', sum)