class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(opening, closing, curr):
            if opening < n:
                backtrack(opening + 1, closing, curr + "(")
            if closing < opening:
                backtrack(opening, closing + 1, curr + ")")
            if closing == opening == n:
                result.append(curr)
        backtrack(0, 0, "")
        return result
