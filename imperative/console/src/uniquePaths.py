class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dpRows = [1] * n
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dpRows[j] += dpRows[j + 1]
        return dpRows[0]
