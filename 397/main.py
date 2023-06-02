#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n == 3:  # 只有最终收敛到3时有一个特例
                return count + 2
            count += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1:
                n -= 1
            else:
                n += 1
        return count
# @lc code=end

