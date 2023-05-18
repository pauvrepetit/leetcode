from typing import List
#
# @lc app=leetcode.cn id=1073 lang=python3
#
# [1073] 负二进制数相加
#

# @lc code=start
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = [0 for _ in range(2 + max(len(arr1), len(arr2)))]
        for i in range(len(arr1)):
            res[-i-1] += arr1[-i-1]
        for i in range(len(arr2)):
            res[-i-1] += arr2[-i-1]
        i = len(res) - 1
        while i > 0:
            if res[i] == 2:
                res[i] = 0
                res[i-1] -= 1
            elif res[i] == 3:
                res[i] = 1
                res[i-1] -= 1
            elif res[i] == -1:
                res[i] = 1
                res[i-1] += 1
            i -= 1
        while res[0] == 0:
            res.pop(0)
            if len(res) == 0:
                return [0]
        return res
# @lc code=end

print(Solution().addNegabinary([1], [1]))