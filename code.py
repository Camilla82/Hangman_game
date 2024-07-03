

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

 
import random
from hangman_words import word_list # import the word_list from hangman_words.py 
from hangman_art import logo, stages # import the logo and stages images from hangman_art.py

end_of_game = False

print(logo)
chosen_word = random.choice(word_list) #This line selects a random word from the word_list
word_length = len(chosen_word) #This line calculates the length of the chosen word and stores it in the variable word_length.

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6 #set number of lives at the start of the game

#Testing code
print(f'Pssst, the solution is {chosen_word}.') # this is to test our code 

#Create blanks
display = [] #create list name display
for _ in range(word_length):
    display += "_" # looping for each letter in the list and add a "_". 

while not end_of_game: #creating a condition: until the game is not finished, do this. 
    guess = input("Guess a letter: ").lower()  # question to the player
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess is display:
      print(f"You have already guessed {guess}")

  
    #Check guessed letter
    for position in range(word_length): #looping through each letter
        letter = chosen_word[position]  # 
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") # print this. 
        if letter == guess: # if the choosen letter is equal to the looped letter
            display[position] = letter # substitute the choosen letter to the appropriate place in the display list. 

    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word: 
        print(f"You guessed {guess}, that is not in the word. You lose a life.)
        lives -= 1 # if the guessed letter is not in the choosen word, reduce lives of 1. 
        if lives == 0: # if lives = 0, the game is over.
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}") 

    #Check if user has got all letters.
    if "_" not in display: # if no more spaces, the game is over and you won. 
        end_of_game = True
        print("You win.") 

   
