# 面试题 01.04. 回文排列
#
# 20200810
# huao

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        flag = 0
        while s != '':
            if s.count(s[0]) % 2 == 1 and flag == 0:
                flag = 1
            elif s.count(s[0]) % 2 == 1 and flag == 1:
                return False
            s = s.replace(s[0], '')
        return True


sol = Solution()
print(sol.canPermutePalindrome("tactcoa"))
