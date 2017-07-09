import random

with open("words.txt", "r+") as f:
	word_list = [line.strip().split() for line in f]
	# print fdata


def word_picker(word_list):
	# this chooses the random word from the fdata list
	choice = random.choice(word_list)
	words_used = []
	while choice in words_used:
		continue
	else:
		words_used.append(choice)
		return choice






