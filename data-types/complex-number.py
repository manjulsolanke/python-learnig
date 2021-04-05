f=10+20j
print(type(f))
print(f.real) # real part is 10
print(f.imag) # imaginary value is 20
x=0B1111 + 10j
print(x)
z=0xface + 15j
print(z)
y=12+0B1111 # invalid, imaginary part should be number
print(y)
