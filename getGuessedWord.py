def getGuessedWord(secretWord, lettersGuessed):
    x = secretWord
    for n in range(len(secretWord)):
        if secretWord[n] not in str(lettersGuessed):
            x = x.replace(secretWord[n], '_ ')
    return x