from typing import List
#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from queue import Queue

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = Queue()
        q.put(('(', 1, 1))
        result = []
        while not q.empty():
            s, cnt, cnt_left = q.get()
            if cnt == n:
                result.append(s + ')' * cnt_left)
            elif cnt_left != 0:
                q.put((s+')', cnt, cnt_left-1))
                q.put((s+'(', cnt+1, cnt_left+1))
            else:
                q.put((s+'(', cnt+1, cnt_left+1))
        return result

# @lc code=end

print(Solution().generateParenthesis(3))

# 这个题我们拿着BFS的思路做，都不知道合不合理，但是动态规划的话，有点问题，不知道怎么弄
