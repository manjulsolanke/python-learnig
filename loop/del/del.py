s1='foo'
s2 = s1
s3 = s2
del s1 # deleted, eligible  for GC. 
print(s2)
print(s3)
