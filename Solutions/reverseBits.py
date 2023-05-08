class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32): # It's fine to hardcode this given the problem statement
            bit = (n >> i) & 1
            res |= (bit << 31 - i)
        return res