#let's play hangman broooooo

from random import randint
import random


word = ['hello','lamp','computer','table','aerospace','xylophone']
hint = ['a common greeting in English','light-emitting household object','best electronic invention of 20th century','household furniture','a cool industry', 'cool sounding musical instrument']



print ("Let's play hangman!")
turn = int(input("How many guesses allowed?		"))
score = 0


while turn > 0:

	random_index = randint(0,(len(word)-1))
	w = word[random_index]
	hidden= list("x" * len(w))

	print ("")
	print ("".join(hidden))
	print ("hint: " + hint[random_index])
	print ("")

	
	while True:
		c = str.lower(input("What character to guess?   "))
		if len(c) == 1:
			if c.isalpha() == True:
				character_index = w.find(c)
				if character_index != -1:
					while character_index != -1:
						hidden[character_index] = c
						#sam input
						character_index = w.find(c, character_index + 1)
				else:
					turn -= 1
			else:
				print ("Only alphabetic character allowed.")
				print ("")
			
		elif c == w:
			score += 1
			print ("You guessed it! Correct!")
			print ("Current score is %i" % score)
			print ("________")
			break

		else:
			print ("You have entered multiple characters, only enter one character.")
			print ("")

		print ("")
		print ("".join(hidden))
		print ("Turns left: %i" % turn)
		print ("")

		if "".join(hidden) == w:
			score += 1
			print ("You win!")
			print ("Current score is %i" % score)
			print ("________")
			break


	if turn == 0:
		print ("You lose.")
		break

#problems :  wrong guess no penalty on turn?
