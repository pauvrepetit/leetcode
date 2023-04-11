#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        forward = 0
        right = 0
        status = 0
        for i in instructions:
            if i == 'L':
                status += 3
            elif i == 'R':
                status += 1
            else:
                if status == 0:
                    forward += 1
                elif status == 1:
                    right += 1
                elif status == 2:
                    forward -= 1
                else:
                    right -= 1
            status %= 4
        return status != 0 or (forward == 0 and right == 0)
# @lc code=end

# 就是一个简单的模拟
