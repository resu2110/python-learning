

wovels = ['a','e','i','o','u']
found_wovel_in_word = []

word = input("come on bitch, write down what you think :V")

for letter in word:
	if(letter in wovels):
		# print("gotcha: ",letter)
		found_wovel_in_word.append(letter)

for letter in found_wovel_in_word:
	print(letter)