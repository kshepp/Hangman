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

#user inputs letter guesses
#limit on guesses
#grab a word for guessing
#check if user input a single letter
#is letter in hidden work? If so, how many times does it appear?
#print the ltters
#add +1 to counter variable if guess is wrong to limit the guesses

# Concepts to keep in mind:
# Random
# Variables
# Boolean
# Input and Output
# Integer
# Char
# String
# Length
# Print



