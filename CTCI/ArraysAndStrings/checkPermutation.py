#Use a hash dict where the keys are the letters and the values are the counts

#Clean up the input, immediately rule them out if the are different lengths

#Place all the characters of string A with their frequencies into an hdict {"letter":freq} O(S)

#Then loop through B, putting their frequencies into a separate hdict 

#Then loop through dict A and make sure that "letter" is in dict B and that "letter":freq
#Is the same for B For every letter
def makeFreqDict(s): #O(S)
    res = dict()
    for char in s:
        if char in res: res[char] += 1
        else: res[char] = 1
    return res
def checkPermutation(s1,s2):
    if len(s1) != len(s2): return False #Clean up the input

    dictA, dictB = makeFreqDict(s1), makeFreqDict(s2)
    for letter in dictA:
        #freqA = dictA[letter]
        #freqB = dictB[letter] Need to use dict.get(key) here to return None if not exists!
        freqA = dictA.get(letter)
        freqB = dictB.get(letter)
        if freqB:
            if freqA != freqB: return False
            else: continue
        else: return False
    return True

if __name__ == "__main__":
    s1 = "hello"
    s2 = "olleh"
    print(checkPermutation(s1,s2))