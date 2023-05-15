class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        resultMap = {}
        l = [0] * 26
        for s in strs:
            for i in range(0, ord('z') - ord('a') + 1):
                l[i] = 0
            for c in s:
                l[ord(c) - ord('a')] += 1
            
            v = tuple(l)
            if v in resultMap:
                resultMap[v].append(s)  
            else:
                resultMap[v] = [s]
        return resultMap.values()
    