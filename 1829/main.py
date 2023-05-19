from typing import List
#
# @lc app=leetcode.cn id=1829 lang=python3
#
# [1829] 每个查询的最大异或值
#

# @lc code=start
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        xor = 0
        for num in nums:
            xor ^= num
        res.append(2 ** maximumBit - xor - 1)
        for i in range(1, len(nums))[::-1]:
            res.append(res[-1] ^ nums[i])
        return res
# @lc code=end

print(Solution().getMaximumXor([0,1,1,3], 2))
