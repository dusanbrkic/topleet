class Solution:
    def hammingWeight(self, n: int) -> int:
        b = 0
        while n > 0:
            if n % 2 == 1:
                b += 1
            n = n >> 1
        return b