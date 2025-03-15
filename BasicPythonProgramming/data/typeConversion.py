# x=int(20)
# y=float(x)
# print(y)



##complex data in, pythion
x = 3+5j
y = 5j
z = -5j
result=x+y
# To convert to float, we need to extract real or imaginary part.
# For example, let's take the real part
p = float(result.real)

print(type(x),x)
print(type(y))
print(type(z))
print(p)