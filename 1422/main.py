#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        score = s.count('1')
        max_score = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                score += 1
            else:
                score -= 1
            max_score = max(score, max_score)
        return max_score

# @lc code=end

print(Solution().maxScore("1111"))