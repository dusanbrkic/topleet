class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        longest = (0, 1)
        longestLength = 1
        
        for i in range(len(s)):
            # odd
            after = i + 1
            before = i - 1
            while after < len(s) and before >= 0:
                if s[after] != s[before]:
                    break
                if after - before + 1 > longestLength:
                    longest = (before, after + 1)
                    longestLength = after - before + 1
                after += 1
                before -= 1
            
            # even
            after = i
            before = i - 1
            while after < len(s) and before >= 0:
                if s[after] != s[before]:
                    break
                if after - before + 1 > longestLength:
                    longest = (before, after + 1)
                    longestLength = after - before + 1
                after += 1
                before -= 1
        return s[longest[0]:longest[1]]