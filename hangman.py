#Hangman game

from random import seed
from random import randint
seed(None) #seed is set based on computer standards

from getpass import getpass

def pick_a_word1():
	wordNum = randint(1, 370099) #find a random number between 1 and the number of words in the file
	wordC = ""
	
	f = open("words_alpha.txt", "r")
	for _ in range(wordNum):
		wordC = f.readline()
	print("Your word has", end=" ")
	print(len(wordC)-1, end=" ")
	print("letters:")
	print("")

	for _ in range(len(wordC)-1):
		print("_", end =" ")
	print("")
	print("")
	return wordC
	
def pick_a_word2():
	wordC = getpass("Input the word to guess (your word will not be shown on the screen):") #get a word from the user
	return wordC + " "
	
def findLet(letter ,arr): #return 1 if it's in there; -1 if it's not
	
	for let in arr:
		if (let == letter):
			return 1
	return 0
	
def printHangman(strike):
	print("--------|") #top
	if(strike > 0):
		print("|      _|_")
		print("|     |___|")
	else:
		print("|")
		print("|")
	
	if(strike == 2):
		print("|       |")
		print("|       |")
		print("|       |")
	elif (strike == 3):
		print("|       |")
		print("|      \|")
		print("|       |")
	elif (strike == 4):
		print("|       |")
		print("|      \|/")
		print("|       |")
	elif (strike == 5): 
		print("|       |")
		print("|      \|/")
		print("|       |")
		print("|      /")
	elif (strike == 6):
		print("|       |")
		print("|      \|/")
		print("|       |")
		print("|      / \ ")
	else:
		print("|")
		print("|")
		print("|")
		print("|")
	print("|")
	print("--------------")
	
	
def play(wordC):
	corrLetters = 0
	strike = 0
	found = [0]*(len(wordC)-1)
	prev = [0]*26
	guessCount = 0
	
	while corrLetters < len(wordC)-1:
		count = 0 #keep track of how many times the guessed letter was found
		if(guessCount != 0):
			print("Previous guesses were", end=" ")
			for i in range(guessCount):
				print(prev[i], end=" ")
			print("")
		letter = input("Guess a letter:") #ask for a letter
		if(len(letter)>1):
			print("Guess must be a single letter")
			print("")
		else:
			if(findLet(letter, prev) == 0):
				prev[guessCount] = letter #save that letter as a previous guess
				guessCount = guessCount+1
				hit = wordC.find(letter) #look for the letter
				while hit != -1:
					found[hit] = 1 #mark that index as found
					count=count+1
					corrLetters=corrLetters+1
					hit = wordC.find(letter, hit+1, len(wordC)-1) #find the next occurrence
				print(letter, end=" ")
				print("was found", end=" ")
				print(count, end=" ")
				print("times.")
				
				if (count == 0):
					strike = strike+1
				
				#print the hangman
				printHangman(strike)
				
				if(strike == 6):
					print("Oh no! You died! Your word was", end=" ")
					print(wordC)
					return
				
				for i in range(len(wordC)-1):
					if (found[i] == 1):
						print(wordC[i], end=" ")
					else:
						print("_", end=" ")
				print("")
				print("")
			else: 
				print("You guessed that already!")
				print("")
		
	print("Congrats! You Won!")



#main

print(" ----------------------------------------------------------")
print("|             ____          ____   ____            ____    |")
print("|    |    |  |      |      |      |    |  |\  /|  |        |")
print("|    |    |  |__    |      |      |    |  | \/ |  |__      |")
print("|    | /\ |  |      |      |      |    |  |    |  |        |")
print("|    |/  \|  |____  |____  |____  |____|  |    |  |____    |")
print("|                                                          |")
print("|                            TO                            |")
print("|           ____            ____            ____           |")
print("|  |    |  |    |  |\   |  |       |\  /|  |    |  |\   |  |")
print("|  |____|  |____|  | \  |  |  __   | \/ |  |____|  | \  |  |")
print("|  |    |  |    |  |  \ |  |    |  |    |  |    |  |  \ |  |")
print("|  |    |  |    |  |   \|  |____|  |    |  |    |  |   \|  |")
print("|                                                          |")
print(" ----------------------------------------------------------")


numPlay = input("Enter number of players (1+): ")
again = "y"
while(again == "y"):
	if(numPlay == "1"):
		word = pick_a_word1()
	else:
		word = pick_a_word2()
	play(word)
	again = input("Want to play again? (y/n) ")
	print("")

print("Thanks for playing!!")
