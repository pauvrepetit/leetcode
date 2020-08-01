# 78. 子集
# 面试题 08.04. 幂集
#
# 20200801
# huao
# 递归，不断的往已有的集合中的每个子集中添加新的元素
# 保证元素添加的顺序就可以了

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        subSet = self.subsets(nums[1:])
        subSetAll = subSet[:]
        for i in subSet:
            ii = i[:]
            ii.append(nums[0])
            subSetAll.append(ii)
        return subSetAll


sol = Solution()
print(sol.subsets([1, 2, 3]))
