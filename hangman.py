#let's play hangman broooooo

from random import randint
import random



word_file = open ("hangman_word.txt", "r")   #words list
word_list = word_file.read().split('\n')

meaning_file = open ("hangman_meaning.txt", "r")   #meaning list
meaning_list = meaning_file.read().split('\n')

print ("Let's play hangman! \nYou have 10 guesses.")
turn =  10 #10 guesses
score = 0


while turn > 0:
	
	while True:
		used_randint = []
		random_index = randint(0,(len(word_list)-1))
		if random_index not in used_randint:
			used_randint.append(random_index)
			w = word_list[random_index]
			break
	
	
	hidden= list("x" * len(w))
	reveal_list=[]


	print ("")
	print ("".join(hidden))
	print ("meaning: " + meaning_list[random_index])
	print ("input 123 to reveal a letter, turn deducts by one")
	print ("")

	
	while "".join(hidden) != w and turn > 0:
		c = str(input("What character to guess?   "))
		if len(c) == 1:
			if c.isalpha() == True:
				c.lower()
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

		elif c == "123": #reveals a single character

			while True:
				reveal_index = randint(0,(len(w)-1))
				if reveal_index not in reveal_list and hidden[reveal_index] != w[reveal_index]:
					reveal_list.append(reveal_index)
					hidden[reveal_index] = w[reveal_index]
					print ("".join(hidden))
					print ("Turn deducted by 1")
					turn -= 1
					break

			
		elif c == w: #guess whole word
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

		if "".join(hidden) == w: #reveal whole word, win
			score += 1
			print ("You win!")
			print ("Current score is %i" % score)
			print ("________")
			break

if turn == 0:
	print ("You lose.")
	print ("Final score is %i" % score)

	highscore_name = str(input ("Highscore name?   "))
	highscore_file = open("highscore.txt","a")
	entry = highscore_file.write(str(score).zfill(3) + " by " + highscore_name + "\n")
	highscore_file.close()

	load_highscore = open("highscore.txt", "r")
	highscore_list = load_highscore.read().split("\n")
	sorted(highscore_list, key=lambda x:x[:3])

	print ("")
	print ("Top three scorers are ... " + str(highscore_list[:3]))
	print ("Good Game!")



