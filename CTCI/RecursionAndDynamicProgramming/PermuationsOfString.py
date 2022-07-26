from random import choice
from collections import defaultdict

class PermuationsOfString:

    def __init__(self, inputString=None, strLen=5) -> None:
        chars = "abcdefghijklmnopqrstuvwxyz"
        if inputString != None:
            self.letters = inputString
        else:
            self.letters = "".join(choice(chars) for i in range(strLen))
    
    def __str__(self) -> str:
        return self.letters

    def getPermuations(self):
        if not self.letters:
            return None
        if len(self.letters) < 2:
            return [self.letters]

        ans = set()
        lettersRemaining = defaultdict(int)
        for char in self.letters:
            lettersRemaining[char] += 1

        def helper(currString):
            if len(currString) == len(self.letters):
                ans.add("".join(currString))
            else:
                for char in lettersRemaining:
                    if lettersRemaining[char] > 0:
                        currString.append(char)
                        lettersRemaining[char] -= 1
                        helper(currString)
                        lettersRemaining[char] += 1
                        currString.pop()
        
        helper([])
        return list(ans)

if __name__ == "__main__":
    numTests = 10
    for test in range(numTests):
        string = PermuationsOfString()
        print(f"string = {string}")
        print(string.getPermuations())