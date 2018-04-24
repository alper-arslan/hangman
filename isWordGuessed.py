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
