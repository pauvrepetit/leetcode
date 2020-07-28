# xh-1.2. 求数组左边的重复数 II
#
# 20200728
# huao
# 这题目好奇怪啊，为啥我的提交记录里面貌似包含了这个题目的所有提交记录呢...
# 题目其实是很简单的就是了

from typing import List

class Solution:
    def find_left_repeat_numII(self, nums: List[int]) -> List[int]:
        numDic = {}
        numLoc = []
        count = 0
        for num in nums:
            if num in numDic.keys():
                numLoc.append(numDic[num])
                numDic[num] = count
            else:
                numLoc.append(-1)
                numDic[num] = count
            count += 1
        return numLoc


sol = Solution()
print(sol.find_left_repeat_numII([1, 3, 1, 2, 1]))
