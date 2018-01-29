class Egg:
	def __init__(self, kind = "scrambled"):
		self.kind = kind
	def whatKind(self):
		return self.kind
def main():
	scrambled = Egg()
	fried = Egg("fried")
	sunnyside =Egg("sunnyside")
	print(scrambled.whatKind())
	print(sunnyside.whatKind())

if __name__ == "__main__": main()
