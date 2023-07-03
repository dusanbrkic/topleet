class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0b0
        
        for n in nums:
            result = result ^ bin(n)
            
        return int(result)