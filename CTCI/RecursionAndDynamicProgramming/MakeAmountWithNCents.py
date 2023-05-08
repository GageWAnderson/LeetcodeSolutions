from random import randint, choices

class Coins:

    """
    Takes in a list of coin values and finds
    the number of unique ways to make an amount using them.
    """
    def __init__(self, coins) -> None:
        self.coins = sorted(coins)
    
    def __str__(self) -> str:
        return str(self.coins)
    
    def countWaysToMakeAmount(self, amount):

        def helper(amountSoFar):
            if amountSoFar == amount:
                return 1
            elif amountSoFar > amount:
                return 0
            else:
                ans = 0
                for coin in self.coins:
                    ans += helper(amountSoFar + coin)
                return ans
        
        return helper(0)

if __name__ == "__main__":
    numTests = 10
    maxAmount = 100
    for test in range(1, numTests + 1):
        nums = choices(range(1, maxAmount), k = 5)
        coins = Coins(nums)
        amount = randint(1, maxAmount)
        print(f"amount = {amount}, coins = {coins}")
        print(coins.countWaysToMakeAmount(randint(1, maxAmount)))