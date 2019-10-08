import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        re_str = '^' + p + '$'
        match = re.search(re_str, s)
        if match == None:
            return False
        return True

sol = Solution()
print(sol.isMatch('aa', 'a'))
print(sol.isMatch('ab', '.*'))
print(sol.isMatch('aa', 'a*'))
