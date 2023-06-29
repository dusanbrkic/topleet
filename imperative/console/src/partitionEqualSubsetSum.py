class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsSum = sum(nums)
        if numsSum % 2 == 1:
            return False
        
        target = numsSum // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums) - 1, -1, -1):
            for t in dp.copy():
                if nums[i] + t == target:
                    return True
                dp.add(nums[i] + t)
        
        return False
                