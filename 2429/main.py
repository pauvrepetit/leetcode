#
# @lc app=leetcode.cn id=2429 lang=python3
#
# [2429] 最小 XOR
#

# @lc code=start
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count1 = bin(num1).count('1')
        count2 = bin(num2).count('1')
        str1 = '0' * 32 + bin(num1)[2:]
        if count2 == 0:
            return 0
        if count1 > count2:
            count2 = count1 - count2
            i = 0
            for j in range(len(str1)):
                if str1[-j-1] == '1':
                    i += 1
                if i == count2:
                    str1 = str1[:-j-1] + '0' * (j + 1)
                    return int(str1, 2)
        count1 = count2 - count1
        if count1 == 0:
            return num1
        i = 0
        for j in range(len(str1)):
            if str1[-j-1] == '0':
                i += 1
            if i == count1:
                str1 = str1[:-j-1] + '1' * (j + 1)
                return int(str1, 2)
        return 0

# @lc code=end

print(Solution().minimizeXor(25, 72))
