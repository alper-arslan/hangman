# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:48:07 2018

@author: MagneticFields
"""

# for taking too many bearks from studying, I decided to start over the hangman
# game
letters_guessed = [] # Guessed letters will be stored here
def get_available_letters(letters_guessed):
    import string
    avail_Letters = string.ascii_lowercase
    availLetters_list = list(avail_Letters)
    for i in range(len(letters_guessed)):
        if letters_guessed[i] in availLetters_list:
            temp = str(letters_guessed[i])
            availLetters_list.remove(temp)
    avail_Letters = "".join(availLetters_list)
    return avail_Letters

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_list = list(secret_word)
    trueCount = 0
    for i in range(len(secret_word_list)):
        if secret_word_list[i] in letters_guessed:
            trueCount += 1
    if trueCount == len(secret_word):
        return True
    else:
return False

def word_guessed(guess):
    
    """
    this checks the user input guess if it is entered before
    """    
    if guess not in letters_guessed:
        return False
    else:
        return True
def hangman(secret_word):
    number_of_guesses = 8 # left guesses will be stored here
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-------------")
    print("You have", str(number_of_guesses), "guesses left.")
    print("Available letters: ", get_available_letters(letters_guessed))
    while True:
        guess_raw = input("Please guess a letter: ")
        guess = guess_raw.lower()
        if word_guessed(guess) is False:
            letters_guessed.append(guess)
        else:
            guess_raw = input("Oops! You've already guessed that letter: ")
            guess = guess_raw.lower()
            
    
