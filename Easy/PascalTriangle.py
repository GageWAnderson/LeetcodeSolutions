# Pascal's Triangle is the embodiment of DP
# This is an excellent, fast DP solution
class Solution:
    def generate(self, numRows: int):
        ans = []
        for i in range(1, numRows + 1):
            row = [0 for i in range(i)]
            row[0], row[-1] = 1, 1
            for j in range(1, i - 1):
                prevRow = ans[-1]
                row[j] = prevRow[j] + prevRow[j - 1]
            ans.append(row)
        return ans

if __name__ == "__main__":
    n = 10
    s = Solution()
    print(s.generate(n)[-1])