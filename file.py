f=open("textfile.txt", "w+")
for i in range(10):
	f.write("This is line %d\r\n" % (i+1))
	print f;
# The file works! \o/

f = open("textfile.txt", "r")
if f.mode == 'r':
	contents = f.read()
	print contents;
	fl = f.readlines()
	for x in fl:
		print x;
