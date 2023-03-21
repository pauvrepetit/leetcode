from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_scores = [(ages[i], scores[i]) for i in range(len(ages))]
        age_scores.sort()
        max_scores = [age_scores[0][1]]    # max_scores[i] 表示 第i个人分数最高的队伍中分数最大的得分
        for i in range(1, len(ages)):
            local_max_score = age_scores[i][1]
            for j in range(i):
                if age_scores[i][1] >= age_scores[j][1]:
                    local_max_score = max(local_max_score, age_scores[i][1] + max_scores[j])
            max_scores.append(local_max_score)
        return max(max_scores)

print(Solution().bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))
print(Solution().bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))
print(Solution().bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1]))

# 动态规划，说实话，我写了这么多题，慢慢也了解了一些动态规划是啥了，哈哈哈哈哈
