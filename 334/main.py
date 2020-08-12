# 334. 递增的三元子序列
#
# 20200812
# huao
# 保存当前最小的一元子序列和二元子序列

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        oneNum = nums[0]
        twoNum = []
        for num in nums[1:]:
            if twoNum == []:
                if num > oneNum:
                    twoNum = [oneNum, num]
                else:
                    oneNum = num
            else:
                if num > twoNum[1]:
                    return True
                elif num > twoNum[0] and num < twoNum[1]:
                    twoNum[1] = num

                if num <= oneNum:
                    oneNum = num
                elif num <= twoNum[0]:
                    twoNum = [oneNum, num]
        return False
