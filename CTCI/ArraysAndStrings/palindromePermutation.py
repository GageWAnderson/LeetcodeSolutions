#CTCI 1.4

#Need an even number of all the letters except for one
#Keep track of frequencies in a dictionary (this implementation ignores non-letter characters)
from collections import Counter #Use this as a builtin for freqDict!
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

def palindromePermutationBetter(s): #Uses collections.Counter as freqDict
    #Algo is case-sensitive
    frequencies = Counter() #This is a bag/multiset
    for char in s:
        freq = frequencies.get(char) #Default is 0
        if freq: frequencies[char] += 1
        else: frequencies[char] = 1

    oddCount = 0
    for letter in frequencies:
        if oddCount > 1: return False
        if frequencies[letter] % 2 == 1: oddCount += 1
    return True

if __name__ == "__main__":
    print(palindromePermutationBetter("tact coa"))
    print(palindromePermutationBetter("RacEArC"))

#Solution notes:
#Must have even counts of all characters (expect for 1)

#We can't optimize big O runtime here since we need to examine all the characters 
#At least once

#OPTIMIZATION: Can check for odd counts as you go along in the problem
#OPTIMIZATION: Use a bitvector of length AlphabetSize to keep track of even/odd
#Final result should only have one 1 in it (bitshift to figure this out)

#Common error on these types of problems:
#"In order to check if A is in group B," I must know everything that is in B
#and then check if one of the items is equal to A"

#You don't need to check all of these if you know the properties of group B, you
#Can check if A matches those properties in an efficient way and if it doesn't
#Remove A from consideration!