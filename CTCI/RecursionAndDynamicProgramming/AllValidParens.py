class AllValidParens:
    def getAllValidParenSequences(n):
        ans = []

        def helper(parens, openParenStack, nOpen, nClosed):
            if len(parens) == 2*n:
                ans.append("".join(parens))
            else:
                if nOpen > 0:
                    parens.append("(")
                    helper(parens, openParenStack + 1, nOpen - 1, nClosed)
                    parens.pop()
                if nClosed > 0 and openParenStack > 0:
                    parens.append(")")
                    helper(parens, openParenStack - 1, nOpen, nClosed - 1)
                    parens.pop()
        
        helper([], 0, n, n)
        return ans

if __name__ == "__main__":
    numTests = 5
    for test in range(1, numTests + 1):
        print(AllValidParens.getAllValidParenSequences(test))
                
