from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            begin = l[i]
            end = r[i]
            sub_nums = nums[begin:end+1]
            sub_nums.sort()
            for j in range(end-begin):
                if sub_nums[j+1]-sub_nums[j] != sub_nums[1]-sub_nums[0]:
                    result.append(False)
                    break
            else:
                result.append(True)
        return result

print(Solution().checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))
print(Solution().checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]))
