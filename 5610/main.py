# 5610. 有序数组中差绝对值之和

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 2
        begin = 0
        for i in range(1, len(nums)):
            begin += (nums[i] - nums[0])
        
        res = [begin]

        for i in range(1, len(nums)):
            res.append(res[i-1] - (nums[i] - nums[i-1]) * (right - left))
            left += 1
            right -= 1
        
        return res
