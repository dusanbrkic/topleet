class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        if l == r:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[r]:
                if target > nums[mid]:
                    if target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[mid]:
                    l = mid + 1
                else:
                    if target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1
        
        return -1
            
                