class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(current, i, s):
            if s > target or i >= len(candidates):
                return
            elif s == target:
                result.append(current)
                return
            
            backtrack(current + [candidates[i]], i, s + candidates[i])
            backtrack(current, i + 1, s)
            
        backtrack([], 0, 0)
        return result
