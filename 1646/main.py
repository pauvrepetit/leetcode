# 1646. 获取生成数组中的最大值
#
# 20210823
# huao

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0 for i in range(n + 1)]
        nums[1] = 1
        max_num = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
            max_num = max(max_num, nums[i])
        return max_num
