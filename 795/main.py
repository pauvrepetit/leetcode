from typing import List
#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#

# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        sub_nums = []
        sub = []
        for num in nums:
            if num > right:
                if sub != []:
                    sub_nums.append(sub)
                    sub = []
            else:
                sub.append(num)
        if sub != []:
            sub_nums.append(sub)
        
        count = 0
        for sub in sub_nums:
            for i in range(len(sub)):
                if sub[i] >= left:
                    count += len(sub) - i
                else:
                    for j in range(i+1, len(sub)):
                        if sub[j] >= left:
                            count += len(sub) - j
                            break
        return count
# @lc code=end

print(Solution().numSubarrayBoundedMax(nums = [2,9,2,5,6], left = 2, right = 8))
