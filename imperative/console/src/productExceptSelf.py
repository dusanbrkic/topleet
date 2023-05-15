class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        prefixProduct = 1
        for i in range(0, len(nums)):
            result[i] = prefixProduct
            prefixProduct *= nums[i]
        postfixProduct = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfixProduct
            postfixProduct *= nums[i]
        return result