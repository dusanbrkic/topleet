class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        buckets = [[] for i in range(0, len(nums))]
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num, -1)
        for key, value in map.items():
            buckets[value].append(key)
        result = []
        for i in range(len(nums) - 1, -1, -1):
            for el in buckets[i]:
                result.append(el)
                if len(result) == k:
                    return result
        return result
