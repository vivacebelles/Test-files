#creates iterations

def isprime(n):
	if n == 1:
		return False
	for x in range(2,n):
		if n % x == 0:
			return False
	else:
		return True

def primes(n = 1):
	while(True):
		if isprime(n): yield n
		n += 1
for n in primes():
	if n > 50: break
	print (n) 

def countdown():
	i=10
	while i>0:
		yield i
		i -= 1

for i in countdown():
	print(i)
