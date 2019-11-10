def getAvailableLetters(lettersGuessed):
    import string
    a = string.ascii_lowercase
    for b in string.ascii_lowercase:
        if b in str(lettersGuessed):
            a = a.replace(b, '')
    return a