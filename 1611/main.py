#
# @lc app=leetcode.cn id=1611 lang=python3
#
# [1611] 使整数变为 0 的最少操作次数
#

# @lc code=start
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        s = bin(n)[2:][::-1]
        count = 2 ** len(s) - 1
        flag = -1
        for i in range(len(s) - 1)[::-1]:
            if s[i] == '1':
                count += (2 ** (i + 1) - 1) * flag
                flag *= -1
        return count
# @lc code=end

print(Solution().minimumOneBitOperations(333))
print(Solution().minimumOneBitOperations(6))
print(Solution().minimumOneBitOperations(9))

# 他就是有一套变换的规则
