s = "This is a string!"
print(s)

l= "You can have new lines with \na touch of a button!"
print(l)

n = 42
s = "This is a {} string!".format(n)
print(s)

j = "Why was nine scared of seven?"
print (j)

x = "Seven {} {}".format(8, 9)
print(x)

a = "Why can you not trust atoms?"
print(a)
m,p = "make up","everything"
print(f"Because they {m}{p}")

print("Now it's on to string functions!")
class bunny:
	def __init__(self, n):
		self.n = n
	def __repr__(self):
		return f"the number of bunnies is {self.n}"

x = bunny(32)
print(x)
