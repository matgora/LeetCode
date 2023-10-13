import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        i = 0
        j = len(s) - 1
        while len(s)/2 > i:
            if s[i] != s[j]:
                return False
            i = i + 1
            j = j - 1
        return True