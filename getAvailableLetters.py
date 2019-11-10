def getAvailableLetters(lettersGuessed):
    import string
    x = string.ascii_lowercase
    for n in range(len(string.ascii_lowercase)):
        if string.ascii_lowercase[n] in str(lettersGuessed):
            x = x.replace(string.ascii_lowercase[n], '')
    return x