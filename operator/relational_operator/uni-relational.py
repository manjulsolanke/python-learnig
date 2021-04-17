# unicode comparison for alphabets 
s1 = 'foo'
s2 = 'baar'
print(s1 <  s2)
print(s1 <= s2)
print(s1 >  s2)
print(s1 >= s2)


# unicode comparison of same name
s1 = 'foo'
s2 = 'foo'
print(s1 <  s2)
print(s1 <= s2)
print(s1 >  s2)
print(s1 >= s2)


# unicode comaprison of capitla nad small alphabets
s1 = 'foo'
s2 = 'Foo'
print("Unicode value of samll f is:", ord('f'))
print("Unicodegit  value of capital F is:", ord('F'))
print(s1 <  s2)
print(s1 <= s2)
print(s1 >  s2)
print(s1 >= s2)
print("\n")

# Boolean value comparison
print("Boolean value comparison \n")
print(True > False)
print(True >= False)
print(True < False)
print(True <= False)
