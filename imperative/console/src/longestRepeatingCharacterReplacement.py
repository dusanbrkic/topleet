class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        start = 0
        total = 0
        maxFrequency = 0
        for i in range(len(s)):
            charMap[s[i]] = charMap.get(s[i], 0) + 1
            maxFrequency = max(maxFrequency, charMap[s[i]])
            
            if i - start + 1 - maxFrequency > k:
                charMap[s[start]] -= 1
                start += 1
        
            total = max(total, i - start + 1)
                    
        return total