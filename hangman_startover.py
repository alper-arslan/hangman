# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:48:07 2018

@author: MagneticFields
"""

# for taking too many bearks from studying, I decided to start over the hangman
# game
lettersGuessed = [] # Guessed letters will be stored here
def getAvailableLetters(lettersGuessed):
    import string
    availLetters = string.ascii_lowercase
    availLetters_list = list(availLetters)
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in availLetters_list:
            temp = str(lettersGuessed[i])
            availLetters_list.remove(temp)
    availLetters = "".join(availLetters_list)
    return availLetters

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord_list = list(secretWord)
    trueCount = 0
    for i in range(len(secretWord_list)):
        if secretWord_list[i] in lettersGuessed:
            trueCount += 1
    if trueCount == len(secretWord):
        return True
    else:
return False

def wordGuessed(guess):
    
    """
    this checks the user input guess if it is entered before
    """    
    if guess not in lettersGuessed:
        return False
    else:
        return True
def hangman(secretWord):
    number_of_guesses = 8 # left guesses will be stored here
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-------------")
    print("You have", str(number_of_guesses), "guesses left.")
    print("Available letters: ", getAvailableLetters(lettersGuessed))
    while True:
        guess_raw = input("Please guess a letter: ")
        guess = guess_raw.lower()
        if wordGuessed(guess) is False:
            lettersGuessed.append(guess)
        else:
            guess_raw = input("Oops! You've already guessed that letter: ")
            guess = guess_raw.lower()
            
    
