#Going to practice some string objects

print("Hello, World.")
print("Hello, World.".upper())
print("Hello, World.".swapcase())
print("Hello, World.".lower())
s1 = "Print World".upper()
s2 = s1.lower()
print(id(s1))
print(id(s2))

s1 = "Hello world."
s2 = "I am here!"
print( s1 + s2) 

#Time to format strings
x = 42
print("The number is always {}".format(x))
