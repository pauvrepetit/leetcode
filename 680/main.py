#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文串 II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                new_s1 = s[:i] + s[i+1:]
                if i == 0:
                    new_s2 = s[:-i-1]
                else:
                    new_s2 = s[:-i-1] + s[-i:]
                return new_s1 == new_s1[::-1] or new_s2 == new_s2[::-1]
        return True
# @lc code=end

print(Solution().validPalindrome("recce"))