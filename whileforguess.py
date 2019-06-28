#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive): ")
guesses = 0
print('aRandomNumber')
print(aRandomNumber)
while guess < 3:
	if guess == aRandomNumber:
		print ("success")
	guesses+=1
	print (guessess)
