#CTCI 1.4

#Need an even number of all the letters except for one
#Keep track of frequencies in a dictionary (this implementation ignores non-letter characters)

def palindromePermutation(str):
    s = str.lower() #Start with lower case
    freqDict = dict()
    for char in s:
        freq = freqDict.get(char)
        if freq: freqDict[char] += 1
        else: freqDict[char] = 1

    print(freqDict) #Issue is lower and upper case hash differently in freqDict
    #Because they have different ASCII values -> for this implementation I will
    #View all chars as the same, so I will make them all lower case
    
    oddCount = 0
    for letter in freqDict:
        if oddCount > 1: return False
        if freqDict[letter] % 2 == 1: oddCount += 1
    return True

if __name__ == "__main__":
    print(palindromePermutation("Tact Coa"))
    print(palindromePermutation("RacEArC"))