class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        largest = 0
        for i in range(0, len(heights)):
            popped = None
            while stack != [] and stack[-1][1] > heights[i]:
                popped = stack.pop()
                largest = max(largest, (i - popped[0]) * popped[1])
            
            try:
                stack.append((popped[0], heights[i]))
            except TypeError:
                stack.append((i, heights[i]))
        
        while stack != []:
            popped = stack.pop()
            largest = max(largest, (len(heights) - popped[0]) * popped[1])

        return largest
