from typing import List

#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#

# @lc code=start
class Solution:
    def match(self, query: str, pattern: str) -> bool:
        i = 0
        j = 0
        pattern += "."
        while i < len(query):
            if query[i] == pattern[j]:
                i += 1
                j += 1
            elif query[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                return False
            else:
                i += 1
        return j == len(pattern) - 1

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.match(query, pattern) for query in queries]
# @lc code=end

print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"))
print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"))
print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"))
