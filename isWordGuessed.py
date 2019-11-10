def isWordGuessed(secretWord, lettersGuessed):
    correctLetter = 0
    for n in range(len(secretWord)):
        if secretWord[n] in lettersGuessed:
            correctLetter += 1
        if correctLetter == n:
            return False
    return True