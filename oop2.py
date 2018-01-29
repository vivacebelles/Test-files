class AnimalActions:
	def quack(self): return self.strings['quack']
	def feathers(self): return self.strings['feathers']
	def bark(self): return self.strings['bark']
	def fur(self): return self.strings['fur']

class Duck(AnimalActions):
	strings = dict(
		quack = "Quaaaaaak!"
		feathers = "The duck has beautiful white and gray feathers."
		bark = "The duck cannot bark"
		fur = "The duck has no fur"

class Person(AnimalActions):
	
