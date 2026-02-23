from core import buildRegex, filterWordList, sortWords, printResults
from utils import downloadWords, validateFound, validateInclude, validateExclude, validateNotAtPos
import tkinter as tk

def solve(foundBoxes, includeBox, excludeBox, excludeBoxes, output):
    fullList = downloadWords()
    wordList = []
    for word in fullList:
        wordList.append(word.lower())
    wordList = list(set(wordList))

    found = list(getFoundWord(foundBoxes).lower())
    if not validateFound(found):
        exit()
        
    include = list(includeBox.get().lower())
    if not validateInclude(include):
        exit()

    exclude = excludeBox.get().lower()
    if not validateExclude(exclude):
        exit()
        
    notAtPos = []
    for i in range(len(found)):
        notAtPos.append(excludeBoxes[i].get().lower())
    if not validateNotAtPos(notAtPos):
        exit()


    patternAsString, pattern = buildRegex(found, include, exclude, notAtPos)
    words = filterWordList(wordList, pattern)

    if (len(words) == 0):
        print("No words found!")
        exit()

    maxFrequency, sortedWords = sortWords(words)

    printResults(patternAsString, len(words), maxFrequency, sortedWords, output)
    

def getFoundWord(foundBoxes):
    chars = []
    for foundBox in foundBoxes:
        char = foundBox.get().strip()
        chars.append(char if char else "-")
    return ''.join(chars)


def updateFoundBox(currText, foundBoxName, window):
    foundBox = window.nametowidget(foundBoxName)

    if currText == '':
        return True

    if len(currText) <= 1 and currText.isalpha():
        return True

    foundBox.configure(validate="none")

    if currText[-1].isalpha() and not currText[-1] == ' ':
        foundBox.delete(0, tk.END)
        foundBox.insert(0, currText[-1])
            
    foundBox.configure(validate="key")
    return False
