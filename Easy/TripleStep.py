class TripleStep:
    def countSteps(n):

        def stepHelper(height):
            if height == n:
                return 1
            elif height < n:
                return stepHelper(height + 1) + stepHelper(height + 2) + stepHelper(height + 3)
            else:
                return 0

        if n < 1:
            return 0
        return stepHelper(0)

if __name__ == "__main__":
    for n in range(40):
        print(f"n = {n}: number of ways = {TripleStep.countSteps(n)}")