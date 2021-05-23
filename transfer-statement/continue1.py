cart = [10,20,600,30,700,80,90]
for item in cart:
    if item > 500:
        print('Insurance must be required, just skipping item')
        continue
    print('Processing item:', item)