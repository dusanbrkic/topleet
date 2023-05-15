class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        maxL = 0
        for num in nums:
            if num - 1 not in s:
                l = 1
                while num + l in s:
                    l += 1
                maxL = max(l, maxL)
        return maxL