class Solution:
    def findSum(self, nums):
        memo = {}
        mod = 1e9 + 7

        def backtrack(c, n, sum, curr):
            if (c, n, sum, curr) in memo:
                return memo[(c, n, sum, curr)]
            
            if n == len(nums):
                return sum + curr
            
            if c.isnumeric():
                result = backtrack(nums[n], n + 1, sum, curr * 10 + int(nums[n])) + backtrack("+", n, sum + curr, 0)
                memo[(c, n, sum, curr)] = result
                return result
            
            result = backtrack(nums[n], n + 1, sum, curr * 10 + int(nums[n]))
            memo[(c, n, sum, curr)] = result
            return result
        
        return int(backtrack("", 0, 0, 0) % mod)
