def Hangaroo(secretWord):
    secretWord = secretWord.lower()
    print('Welcome to the game of Hangaroo!')
    lettersGuessed = ['']
    mistakes = 0
    while not isWordGuessed(secretWord, lettersGuessed):
        print('\nMistakes: ', mistakes,'\nMissing letters: \n', getGuessedWord(secretWord, lettersGuessed))
        guess = input('Input your letter of guess: ')
        guessInLowerCase = guess.lower()
        if guessInLowerCase not in lettersGuessed:
            lettersGuessed.append(guessInLowerCase)
            if guessInLowerCase not in secretWord:
                mistakes += 1
                if mistakes == 4:
                    return print('You lost. The kangaroo is hanged  :c')
        else:
            print('\nYou already guessed that letter. Try again!')
    return print('\nSecret Word:', getGuessedWord(secretWord, lettersGuessed),'\nCongratulations, you won!')