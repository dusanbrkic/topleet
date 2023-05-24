class Solution:
    def findMin(self, nums: List[int]) -> int:
        currMin = nums[0]
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            currMin = min(currMin, nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1

        return min(currMin, nums[l])