import nltk

## Check if we already have word list
def downloadWords():
    try:
        nltk.data.find('corpora/words.zip')
    except LookupError:
        print("Downloading words corpus...")
        nltk.download('words')
    from nltk.corpus import words
    return words.words()

# Validate input for found letters
def validateFound(found):
    if len(found) != 5:
        print("Please enter exactly 5 characters!")
        return False
    if not all(ch == '-' or ch.isalpha() for ch in found):
        print("Invalid Characters in Found.")
        return False
    return True

# Validate input for include (must be alphabetic)
def validateInclude(include):
    if not all(char.isalpha() for char in include):
        print("Invalid Characters in Include")
        return False
    return True

# Validate input for exclude (must be alphabetic)
def validateExclude(exclude):
    if not exclude.isalpha() and not ' ':
        print("Invalid Characters in Exclude")
        return False
    return True

# Validate input for not at positions
def validateNotAtPos(notAtPos):
    for i in range(len(notAtPos)):
        if not notAtPos[i].isalpha() and not notAtPos[i] == '':
            print(f"Invalid Character entered for position {i}")
            return False
    return True