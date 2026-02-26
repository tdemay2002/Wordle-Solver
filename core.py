import re
import tkinter as tk
from LetterCountHash import LetterCountHash

# create regular expression
def buildRegex(found, include, exclude, notAtPos):
    includeEx = ""
    for char in include:
        includeEx += f"(?=.*" + char + ")"
    builtEx = "^" + includeEx

    for i in range(len(found)):
        if found[i] != '-':
            builtEx += found[i]
        else:
            if len(exclude) == 0 and len(notAtPos[i]) == 0:
                builtEx += "[a-z]"
            else:
                builtEx += f"[^" + exclude + notAtPos[i] + "]"
    builtEx += "$"
    return builtEx, re.compile(builtEx)


# test regular expression
def filterWordList(wordList, pattern):
    try:
        return [word for word in wordList if re.fullmatch(pattern, word)]
    except:
        print("\nThat is not a valid expression!\n")
        exit()


# find count of each letter in word possibilities
def sortWords(words):
    positionCounts = [LetterCountHash() for _ in range(5)] 

    for word in words:
        for pos, letter in enumerate(word):
            positionCounts[pos].updateCount(letter)

    numOfWords = len(words)

    # creates a position set with alphabet probability subsets
    positionProbs = []
    for pos in range(5):
        positionProb = {}
        for letter, count in positionCounts[pos].letterCounts.items():
            positionProb[letter] = count / numOfWords
        positionProbs.append(positionProb)

    positionMaxFrequency = []
    for pos in range(5):
        letter, frequency = positionCounts[pos].getMax() or (None, 0)
        positionMaxFrequency.append((pos, (letter, frequency)))
    positionMaxFrequency.sort(key=lambda x: x[1][1], reverse=True)

    words = sorted(words)
    def rank_key(word):
        return tuple(
            positionProbs[pos].get(word[pos], 0)
                for pos, _ in positionMaxFrequency
        )
    return positionMaxFrequency, sorted(words, key=rank_key, reverse=True)


def printResults(builtEx, found, textBox, wordsLength = list, maxFrequency = list, sortedWords = list):
    textBox.delete(1.0, tk.END)
    textBox.insert(tk.END, ("Searching for (" + builtEx + ")\n"))
    
    if not found:
        textBox.insert(tk.END, "No words were found! \n" + "\n")
        return
    
    textBox.insert(tk.END, f"{wordsLength} words were found: \n" + "\n")
    textBox.insert(tk.END, "Sort by: " + "\n")
    for i in range(5):
        textBox.insert(tk.END, f"Position {maxFrequency[i][0]}:\n     prioritizes '{maxFrequency[i][1][0]}' with {maxFrequency[i][1][1]} counts." + "\n")
    textBox.insert(tk.END, "\n")
    textBox.insert(tk.END, f"Try: ('{sortedWords[0]}')\n")
    for i, word in enumerate(sortedWords):
        textBox.insert(tk.END, "\'" + word + "\'" + "\n")