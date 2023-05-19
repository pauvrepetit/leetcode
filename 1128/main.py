from typing import List
#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
class Solution:
    def com(self, count: int) -> int:
        return (count - 1) * count // 2


    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in range(len(dominoes)):
            if dominoes[i][0] > dominoes[i][1]:
                dominoes[i] = [dominoes[i][1], dominoes[i][0]]
        dominoes.sort()
        all_count = 0
        count = 1
        for i in range(1, len(dominoes)):
            if dominoes[i] == dominoes[i-1]:
                count += 1
            else:
                all_count += self.com(count)
                count = 1
        all_count += self.com(count)
        return all_count
# @lc code=end

print(Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
