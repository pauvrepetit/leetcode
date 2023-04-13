from typing import List

#
# @lc app=leetcode.cn id=2404 lang=python3
#
# [2404] 出现最频繁的偶数元素
#

# @lc code=start
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = dict()
        for num in nums:
            if num & 0x1 == 1:
                continue
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        max_num = -1
        max_count = 0
        for num in count.keys():
            if count[num] > max_count:
                max_count = count[num]
                max_num = num
            elif count[num] == max_count:
                max_num = min(max_num, num)
        return max_num
# @lc code=end

print(Solution().mostFrequentEven(nums = [0,1,2,2,4,4,1]))
print(Solution().mostFrequentEven(nums = [4,4,4,9,2,4]))
print(Solution().mostFrequentEven([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))
