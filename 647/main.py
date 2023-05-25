#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = 0
        for i in range(length):
            for j in range(i+1, length+1):
                sub_s = s[i:j]
                if sub_s == sub_s[::-1]:
                    count += 1
        return count
# @lc code=end

