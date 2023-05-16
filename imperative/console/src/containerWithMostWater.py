class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        p = 0
        while i < j:
            p = max(p, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]:
                j -= 1
                continue
            
            if height[j] > height[i]:
                i += 1
                continue
            
            if height[j] == height[i]:
                i += 1
                j -= 1
            
        return p