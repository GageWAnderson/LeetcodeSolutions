#CTCI 1.6

#Store sections (strings of repeats) in an array 
# and compress them based on their character, length
#Then loop through the array again and concatenate everything together

def stringCompression(s):
    stringBuilder = []
    runLen = 0 #Keep track of runs of same characters
    for i in range(len(s)):
        if i == 0 or s[i-1] == s[i]: 
            runLen += 1
            if i == len(s) - 1: #Account for the edge case where there is a run at the end
                letter = s[i-1]
                stringBuilder.append(letter + str(runLen))
        else:
            letter = s[i-1]
            stringBuilder.append(letter + str(runLen))
            runLen = 1
    res = ""
    for elem in stringBuilder:
        res = res + elem
    return res

if __name__ == "__main__":
    print(stringCompression("fsadfasdfsadffffffffff"))
    print(stringCompression("AggarwalSadikuIXYou"))

#This string builder array seems like a common plan to minimize concatenation costs...
#Solution notes:

#String concatenation operates in O(n^2) time, so we should use string-builder data structure

