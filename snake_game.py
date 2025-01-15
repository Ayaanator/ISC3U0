def letter_counter(words: list):
	dictionary = {}

	for word in words:
		for char in word:
			dictionary[char] = dictionary.setdefault(char, 0) + 1

	return dictionary


spam = {"title" : 23, "name": "arthur"}
spam["title"] += 5
spam["noob"] = ""

names = {"Talia": 16, "Nabil": 15, "Rogan": 17} 
names["Nolan"] = names.setdefault("Nolan", 0) + 152

names["Nolan"] = names.setdefault("Nolan", 0) + 1253
names[5] = "adads"

print(names)

def mystery(nums: [int]):
	for i in range(len(nums)):
		nums[i] += 2

x = [1,2,3,4]
mystery(x)
print(x)
print(names[5])