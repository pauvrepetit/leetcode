#
# @lc app=leetcode.cn id=2544 lang=python3
#
# [2544] 交替数字和
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        strn = str(n)
        flag = True
        res = 0
        for s in strn:
            if flag:
                res += int(s)
            else:
                res -= int(s)
            flag = not flag
        return res
# @lc code=end

