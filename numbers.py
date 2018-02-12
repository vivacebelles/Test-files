from decimal import *

a = Decimal(".10")
b = Decimal(".30")

x = a + a + a - b
y = 3*a - b
print("x is {}".format(x))
print("y is {}".format(x))
print(type(x,y))

if (x == y):
	print("True! x = y")
else:
	print("No.")
