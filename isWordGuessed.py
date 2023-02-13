def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secret_word_list = list(secret_word)
    true_count = 0
    for i in range(len(secret_word_list)):
        if secret_word_list[i] in letters_guessed:
            true_count += 1
    if true_count == len(secret_word):
        return True
    else:
        return False
