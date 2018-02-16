#so lists are mutable but tuples are immutable

print("Here's a dictionary!")
animals = dict(kitten = "meow", puppy = "woof", lion = "rawr", dragon = "grr")
animals[2] = "Simba"
print(animals[2])

print_dict(animals)
print(animals.get("puppy"))
