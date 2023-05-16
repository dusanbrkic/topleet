class Solution:
    def isPalindrome(self, s: str) -> bool:
        plainS = ""
        for c in s:
            if (ord(c) >= ord("A") and ord(c) <= ord("Z")) or (ord(c) >= ord("a") and ord(c) <= ord("z")) or (ord(c) >= ord("0") and ord(c) <= ord("9")):
                plainS += c.lower()
        print(plainS)
        for i in range(0, len(plainS) // 2):
            if plainS[i] != plainS[len(plainS) - 1 - i]:
                return False
        return True
            