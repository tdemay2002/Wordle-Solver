from core import buildRegex, filterWordList, sortWords, printResults
from utils import downloadWords, validateFound, validateInclude, validateExclude, validateNotAtPos
import tkinter as tk

def solve(foundBoxes, excludeBox, excludeAtBoxes, output):
    fullList = downloadWords()
    wordList = []
    for word in fullList:
        wordList.append(word.lower())
    wordList = list(set(wordList))

    found = list(getFoundWord(foundBoxes).lower())
    if not validateFound(found):
        exit()

    exclude = excludeBox.get().lower()
    if not validateExclude(exclude):
        exit()
        
    notAtPos = []
    for i in range(len(found)):
        notAtPos.append(excludeAtBoxes[i].get().lower())
    if not validateNotAtPos(notAtPos):
        exit()

    include = set("".join(notAtPos))
    if not validateInclude(include):
        exit()

    patternAsString, pattern = buildRegex(found, include, exclude, notAtPos)
    words = filterWordList(wordList, pattern)

    if (len(words) == 0):
        printResults(patternAsString, False, output)
        return
        
    maxFrequency, sortedWords = sortWords(words)

    printResults(patternAsString, True, output, len(words), maxFrequency, sortedWords)
    

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
