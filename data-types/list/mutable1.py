# list is mutable, we can change the value of existing list alike below example.
l1 = [10, 20, 30, 40]
l2 = l1
print(l1)
l1[0] = 7777
l2[1] = 8888
print(l1)
print(l2)

