class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n = len(text2) + 1
        
        dp = [[0] * n for i in range(m)]
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    continue
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]
