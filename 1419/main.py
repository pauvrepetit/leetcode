#
# @lc app=leetcode.cn id=1419 lang=python3
#
# [1419] 数青蛙
#

# @lc code=start
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # 记录当前，c\cr\cro\croa的数量
        min_flogs = 0
        count = [0 for _ in range(4)]
        for c in croakOfFrogs:
            if c == 'c':
                count[0] += 1
            elif c == 'r':
                if count[0] == 0:
                    return -1
                count[0] -= 1
                count[1] += 1
            elif c == 'o':
                if count[1] == 0:
                    return -1
                count[1] -= 1
                count[2] += 1
            elif c == 'a':
                if count[2] == 0:
                    return -1
                count[2] -= 1
                count[3] += 1
            elif c == 'k':
                if count[3] == 0:
                    return -1
                count[3] -= 1
            else:
                return -1
            local_max = sum(count)
            min_flogs = max(min_flogs, local_max)
        if sum(count) != 0:
            return -1
        return min_flogs
        
# @lc code=end

print(Solution().minNumberOfFrogs('crcoakroak'))
