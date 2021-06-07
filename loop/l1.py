cart = [10,20,30,40,50,60]
for item in cart:
    if item > 500:
        print('We cannt place this order')
        break # If break didnt executed then else would execute
    print('processing items:', item)
else:
    print('Congratulations all items are processed successfully')