# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:48:07 2018

@author: Alper
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
def hangman(secretWord):
    number_of_guesses = 8 # left guesses will be stored here
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-------------")
    print("You have", str(number_of_guesses), "guesses left.")
    print("Available letters: ", getAvailableLetters(lettersGuessed))
    