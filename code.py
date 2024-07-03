#Step 4

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

end_of_game = False 
word_list = ["ardvark", "baboon", "camel"]
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

    #Check guessed letter
    for position in range(word_length): #looping through each letter
        letter = chosen_word[position]  # 
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") # print this. 
        if letter == guess: # if the choosen letter is equal to the looped letter
            display[position] = letter # substitute the choosen letter to the appropriate place in the display list. 

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word: 
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

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives]) # This line prints the chosen ASCII art from the stages list based on the current number of lives.
