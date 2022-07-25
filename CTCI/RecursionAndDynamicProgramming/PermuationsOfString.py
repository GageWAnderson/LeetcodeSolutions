from random import choice

class PermuationsOfString:

    def __init__(self, inputString=None, strLen=5) -> None:
        chars = "abcdefghijklmnopqrstuvwxyz"
        if inputString != None:
            self.letters = inputString
        else:
            self.letters = "".join(choice(chars) for i in range(strLen))

    def getPermuations(self):
        if not self.letters:
            return None
        if len(self.letters) < 2:
            return [self.letters]

        ans = []
        lettersRemaining = set()
        for char in self.letters:
            lettersRemaining.add(char)

        def helper(currString):
            if len(currString) == len(self.letters):
                ans.append("".join(currString))
            else:
                for char in lettersRemaining:
                    currString.append(char)
                    lettersRemaining.remove(char)
                    helper(currString)
                    lettersRemaining.add(char)
                    currString.pop()
        
        helper([])
        return ans

if __name__ == "__main__":
    numTests = 10
    for test in range(numTests):
        string = PermuationsOfString()
        print(string.getPermuations())