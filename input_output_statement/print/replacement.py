name = 'foo'
salary = 10000
org = 'GL'
# replacement 
print('hello {}, your salary {}, and your company is {}'.format(name,salary,org))
# indexing 
print('hello "{0}", your salary {1}, and your company is {2}'.format(name,salary,org))
# indexing with keyword
print('hello {n}, your salary {s}, and your company is {o}'.format(n=name,s=salary,o=org))
