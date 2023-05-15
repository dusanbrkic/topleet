class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = "([{"
        closing = ")]}"

        for c in s:
            if c in opening:
                stack.append(c)
            
            if c in closing:
                if stack == [] or opening.find(stack.pop()) != closing.find(c):
                    return False
                
        if stack != []:
            return False
        
        return True