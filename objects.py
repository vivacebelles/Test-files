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

print("now for formatting!")

x = 42
y = 3
print(f"{x:+} and {y:-} are the numbers contained in x and y")

list = "This is a list of words I decided to split."
print(list)
print(list.split())
print(list.split("is"))
print(list.split("t"))
ls2 = ":".join(list)
print(ls2)
