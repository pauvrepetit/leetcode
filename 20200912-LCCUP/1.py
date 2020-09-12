# LCP 17. 速算机器人
# LeetCode CUP 2020 Fall
#
# 20200912
# huao

class Solution:
    def calculate(self, s: str) -> int:
        x = 1
        y = 0
        for i in s:
            if i == 'A':
                x = 2 * x + y
            else:
                y = 2 * y + x
        return x + y


print(Solution().calculate('AB'))
