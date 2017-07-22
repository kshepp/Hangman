import random

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
		letters_used = []

		with open("words.txt", "r+") as f:
			word_list = [line.strip().split() for line in f]
		word_chosen = str(random.choice(word_list)).lower()
		word_chosen = word_chosen[2:-2]

		while guesses < 6:

			for letter in word_chosen:
				if letter in letters_used:
					print letter,
				else:
					hidden_letters = letter.replace(letter, " * ", word_chosen.__len__())
					print hidden_letters,

			guess = raw_input("\n Guess a letter -> \n").lower()

			if guess in letters_used:
				print "Try again, you must choose a letter that you haven't guessed"
				print "Letters used so far:", letters_used.append(guess)

			elif guess in word_chosen:
				if guess == word_chosen:
					print "You win! I'll get you next time."
					break
				else:
					print "You've found a letter!"
					letters_used.append(guess)
					print "Letters used so far:",letters_used
					print "You have ", 6-int(guesses), "guesses left"

			elif guess not in word_chosen:
				print "Ut-oh! I'm drawing"
				letters_used.append(guess)
				self.drawing(guesses)
				print "Letters used so far:",letters_used
				guesses+=1
				print "You have ", 6-int(guesses), "guesses left"
			if guesses == 6:
				print "You lose! The word was: " + word_chosen,



	def drawing(self, guesses):
		if guesses == 0:
			print """ |------"""
			print """ |     |"""
			print """ |     O"""
			print """ |      """
			print """ |      """
			print """ |      """
			print """ |_______ """
		elif guesses == 1:
			print """ |------"""
			print """ |     |"""
			print """ |     O"""
			print """ |     |"""
			print """ |     |"""
			print """ |      """
			print """ |_______ """

		elif guesses == 2:
			print """ |------"""
			print """ |     |"""
			print """ |     O"""
			print """ |   \_|"""
			print """ |     |"""
			print """ |      """
			print """ |_______ """
		elif guesses == 3:
			print """ |------"""
			print """ |     |"""
			print """ |     O"""
			print """ |   \_|_/"""
			print """ |     |"""
			print """ |      """
			print """ |_______ """
		elif guesses == 4:
			print """ |------"""
			print """ |     |"""
			print """ |     O"""
			print """ |   \_|_/"""
			print """ |     |"""
			print """ |    / """
			print """ |_______ """
		elif guesses == 5:
			print """ |------"""
			print """ |     |"""
			print """ |     O"""
			print """ |   \_|_/"""
			print """ |     |"""
			print """ |    / \ """
			print """ |_______ """

Hangman()

#improvements to make:
# 1) if you reveal all the letters make it so you don't have to retype the word to win
