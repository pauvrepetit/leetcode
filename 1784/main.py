#
# @lc app=leetcode.cn id=1784 lang=python3
#
# [1784] 检查二进制字符串字段
#

# @lc code=start
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        length = len(s)
        s += '0'
        for i in range(length):
            if s[i] == '1' and s[i+1] == '0':
                count += 1
                if count == 2:
                    return False
        return True
# @lc code=end

