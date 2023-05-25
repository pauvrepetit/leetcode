#
# @lc app=leetcode.cn id=1876 lang=python3
#
# [1876] 长度为三且各字符不同的子字符串
#

# @lc code=start
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good_count = 0
        for i in range(len(s) - 2):
            sub_s = s[i:i+3]
            if sub_s[0] != sub_s[1] and sub_s[0] != sub_s[2] and sub_s[1] != sub_s[2]:
                good_count += 1
        return good_count
# @lc code=end

