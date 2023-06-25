class Solution:
    def rob(self, nums: List[int]) -> int:
        def robSeq(numsSeq):
            rob1 = 0
            rob2 = 0
            m = 0

            for n in numsSeq:
                m = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = m
            return m

        if len(nums) == 1:
            return nums[0]
        
        return max(robSeq(nums[:-1]), robSeq(nums[1:]))
