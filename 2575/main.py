from typing import List
#
# @lc app=leetcode.cn id=2575 lang=python3
#
# [2575] 找出字符串的可整除数组
#

# @lc code=start
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        num = int(word[0])
        res = [num % m]
        for i in range(1, len(word)):
            num = int(word[i])
            res.append((10 * res[-1] + num) % m)
        for i in range(len(res)):
            res[i] = 1 if res[i] == 0 else 0
        return res

# @lc code=end

