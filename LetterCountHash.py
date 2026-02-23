class LetterCountHash:
    def __init__(self):
        self.letterCounts = {}

    def updateCount(self, letter):
        if letter in self.letterCounts:
            self.letterCounts[letter] += 1
        else:
            self.letterCounts[letter] = 1
    
    def getMax(self):
        if not self.letterCounts:
            return None
        mostCommonLetter = max(self.letterCounts, key=self.letterCounts.get)
        frequency = self.letterCounts[mostCommonLetter]
        return mostCommonLetter, frequency
