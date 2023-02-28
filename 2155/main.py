from typing import List


class Solution:
    # 遍历而已
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        max_i_list = [0]
        max_score = sum(nums)
        now_score = max_score
        for i in range(1, len(nums)+1):
            if nums[i-1] == 0:
                now_score += 1
            else:
                now_score -= 1
            if now_score == max_score:
                max_i_list.append(i)
            elif now_score > max_score:
                max_i_list = [i]
                max_score = now_score
        return max_i_list


print(Solution().maxScoreIndices(nums=[0, 0, 1, 0]))
print(Solution().maxScoreIndices(nums=[0, 0, 0]))
print(Solution().maxScoreIndices(nums=[1, 1]))
