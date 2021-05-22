cart = [10,20,30,600,70,80]
for item in cart:
    if item > 500:
        print("To place this order, insurane must be required")
        break
    print('Processing items:', item)