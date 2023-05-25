from heapq import heappop, heappush

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        zippedNums = []
        for n1, n2 in zip(nums1, nums2):
            zippedNums.append((n1, n2))
        
        zippedNums.sort(reverse=True, key=lambda e: e[1])
        
        heap = []
        total = 0
        result = 0
        for num in zippedNums:
            heappush(heap, num[0])
            total += num[0]
            if len(heap) == k:
                result = max(result, total * num[1])
                total -= heappop(heap)
        
        return result