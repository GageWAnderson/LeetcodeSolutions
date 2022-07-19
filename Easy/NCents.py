class NCents:
    def nCentsCombonations(n):

        memo = {}
        def helper(amount, coinsUsed):
            if tuple(coinsUsed) in memo:
                return memo[tuple(coinsUsed)]
            elif amount == n:
                if tuple(coinsUsed) not in memo:
                    memo[tuple(coinsUsed)] = 1
                    return 1
            elif amount < n:
                if tuple(coinsUsed) not in memo:
                    coinsUsed.append(25)
                    addQuarter = helper(amount + 25, coinsUsed)
                    coinsUsed.pop()
                    coinsUsed.append(10)
                    addDime = helper(amount + 10, coinsUsed)
                    coinsUsed.pop()
                    coinsUsed.append(5)
                    addNickel = helper(amount + 5, coinsUsed)
                    coinsUsed.pop()
                    coinsUsed.append(1)
                    addPenny = helper(amount + 1, coinsUsed)
                    coinsUsed.pop()
                    res = addQuarter + addDime + addNickel + addPenny
                    memo[tuple(coinsUsed)] = res
                    return res
            else:
                return 0
        
        ans = helper(0, [])
        # print(memo)
        return ans

if __name__ == "__main__":
    for test in range(100):
        print(NCents.nCentsCombonations(test))