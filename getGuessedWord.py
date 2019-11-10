def getGuessedWord(secretWord, lettersGuessed):
    a = secretWord
    for b in secretWord:
        if b not in str(lettersGuessed):
            a = a.replace(b, '_ ')
    return a