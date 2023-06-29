class Solution:
    def numDecodings(self, s: str) -> int:
        num2 = 0
        num1 = 1
        
        for i in range(len(s) - 1, -1, -1):
            # one digit
            if s[i] != '0':
                curr = num1
            else:
                curr = 0
            
            # two digits
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                curr += num2
            
            num2 = num1
            num1 = curr
        
        return curr
        