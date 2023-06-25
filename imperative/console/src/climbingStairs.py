class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        first = 2
        second = 3

        for i in range(3, n):
            s = first + second
            first = second
            second = s
        return second