days= ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
for i, d in enumerate(days):
	print (i, d)

a, b = 0, 1
while b < 50:
	print (b)
	a,b = b, a+b

print("Now onto for loops!")

fh = open('lines.txt', 'w+')
for line in fh.readlines():
	print(line, end = ' ')

words = ["hello", "world", "today", "is", "a", "good", "day"

for i in words:
	print(i)
