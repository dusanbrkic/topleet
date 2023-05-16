class Solution:
    def trap(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        mLeft = height[i]
        mRight = height[j]
        drops = 0
        while i < j:
            if mLeft < mRight:          
                i += 1
                lDrops = mLeft - height[i]
                if lDrops > 0:
                    drops += lDrops
                mLeft = max(mLeft, height[i])
            else:
                j -= 1
                rDrops = mRight - height[j]
                if rDrops > 0:
                    drops += rDrops
                mRight = max(mRight, height[j])
        return drops