class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        before = (nums[0], nums[0])
        allMax = nums[0]
        
        for i in range(1, len(nums)):
            curr = (max(nums[i], before[0] * nums[i], before[1] * nums[i]), \
                min(nums[i], before[0] * nums[i], before[1] * nums[i]))
            allMax = max(allMax, curr[0], curr[1])
            before = curr
    
        return allMax