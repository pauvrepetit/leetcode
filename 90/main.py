# 90. 子集 II
#
# 20210716
# huao

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        all_subset_count = 2 ** len(nums)
        all_subsets = []
        for i in range(all_subset_count):
            subset = []
            stri = bin(i)[2:][::-1]
            for j in range(len(stri)):
                if stri[j] == '1':
                    subset.append(nums[j])
            subset.sort()
            all_subsets.append(subset)

        # 接下来我们对all_subsets去重
        all_subsets.sort()
        i = 0
        while i < len(all_subsets) - 1:
            if all_subsets[i] == all_subsets[i + 1]:
                all_subsets.pop(i)
            else:
                i += 1
        return all_subsets


print(Solution().subsetsWithDup(nums=[1, 2, 2]))
print(Solution().subsetsWithDup(nums=[2]))
