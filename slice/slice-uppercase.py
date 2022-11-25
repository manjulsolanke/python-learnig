'''
uppercase and lenght 
'''
s = "manjulsolanke"
print("print the lenth of s:",len(s))
print(s[0:len(s)]) 
# print first charactor in upper case
print("print first charactor in upper case")
output = s[0:len(s)-1]+s[-1].upper()
print(output)

# print first and last character in upper case


print("print first and last character in upper case")
output = s[0].upper() + s[1:len(s) -1] + s[-1].upper()
print(output)