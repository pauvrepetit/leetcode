from typing import List

#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#

# @lc code=start
class Solution:
    def tranfer(self, num: str) -> List[int]:
        for i in range(len(num)):
            if num[i] == '+':
                a = int(num[:i])
                b = int(num[i+1:-1])
                return [a, b]
        return [0, 0]

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = self.tranfer(num1)
        a2, b2 = self.tranfer(num2)
        a = a1 * a2 - b1 * b2
        b = a1 * b2 + a2 * b1
        return "{}+{}i".format(a, b)

# @lc code=end

