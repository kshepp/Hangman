import random

	# print fdata

class Hangman(object):
	def __init__(self):
		print "Welcome to Hangman! Are you ready to play?"
		print "Yes = 1 and No = 2"
		user_choice_to_play = raw_input("-> ")

		if user_choice_to_play == "1":
			print "Loading game"
			self.start_game()
		else:
			print "okay bye!"
			exit()

	def start_game(self):
		print "This is where the scary intro goes"
		self.game()

	def game(self):
		guesses = 0
		letters_used = ""
		with open("words.txt", "r+") as f:
			word_list = [line.strip().split() for line in f]
		# this chooses the random word from the fdata list
		word_chosen = str(random.choice(word_list))
		print word_chosen
		while guesses < 6:
			guess = raw_input("Guess a letter -> ")
			if guess in word_chosen:
				print guess in word_chosen
			# word_chosen.find(guess)


Hangman()

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