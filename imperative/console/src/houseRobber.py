class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1 = 0
        rob2 = 0
        m = 0
        
        for n in nums:
            m = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = m
        
        return m
        
