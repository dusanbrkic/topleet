class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        tMap = {}
        tCount = 0
        for c in t:
            if c not in tMap:
                tCount += 1
                tMap[c] = 1
            else:
                tMap[c] += 1
        
        sMap = {}
        windowCount = 0
        
        l = 0
        total = ("", float('inf'))
        for r in range(len(s)):
            
            if s[r] in tMap:
                sMap[s[r]] = sMap.get(s[r], 0) + 1
                if sMap[s[r]] == tMap[s[r]]:
                    windowCount += 1
                
            while windowCount == tCount:
                total = min(total, (s[l:r+1], r - l + 1), key=lambda e: e[1])
                if s[l] in sMap:
                    if sMap[s[l]] == tMap[s[l]]:
                        windowCount -= 1
                    sMap[s[l]] -= 1
                l += 1
        
        return total[0]
        
        