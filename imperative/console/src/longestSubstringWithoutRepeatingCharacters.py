class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        total = 0
        
        charMap = {}
        for i in range(len(s)):
            if s[i] in charMap:
                start = max(start, charMap[s[i]] + 1)
            total = max(total, i - start + 1)
            charMap[s[i]] = i
        return total