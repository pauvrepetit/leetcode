#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        res_str = ""
        i = 0
        while length > k * 2:
            res_str += (s[i:i+k][::-1] + s[i+k:i+k*2])
            i += k * 2
            length -= k * 2
        if length > k:
            res_str += s[i:i+k][::-1] + s[i+k:]
        else:
            res_str += s[i:][::-1]
        return res_str
# @lc code=end

