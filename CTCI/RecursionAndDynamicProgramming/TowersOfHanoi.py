class TowersOfHanoi:

    def __init__(self, n):
        self.startTower = [(n - num) for num in range(abs(n))]
        self.middleTower = []
        self.endTower = []
    
    def solve(self):

        def helper(n, start, buffer, destination):
            if n == 0:
                return
            else:
                helper(n-1, start, destination, buffer)
                destination.append(start.pop())
                helper(n-1, buffer, start, destination)
        
        helper(len(self.startTower), self.startTower, self.middleTower, self.endTower)
        return self.endTower

if __name__ == "__main__":
    numTests = 10
    for test in range(numTests):
        towers = TowersOfHanoi(test)
        print(f"Solving Towers of Hanoi for n = {test}")
        print(f"result = {towers.solve()}")