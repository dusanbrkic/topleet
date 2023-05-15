class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        results = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            while True:
                if stack != [] and temperatures[stack[-1]] < temperatures[i]:
                    popped = stack.pop()
                    results[popped] = i - popped
                else:
                    stack.append(i)
                    break
        
        return results
        
