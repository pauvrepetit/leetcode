#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def checkCount(self, count) -> bool:
        for val in count.values():
            if val < 0:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        begin = 0
        end = len(t)
        count = dict()
        for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count[c] = 0
        for c in t:
            count[c] -= 1
        for c in s[begin:end]:
            count[c] += 1
        if self.checkCount(count):
            return s[begin:end]
        res = ""
        while end < len(s):
            if not self.checkCount(count):
                count[s[end]] += 1
                end += 1
                if self.checkCount(count):
                    while count[s[begin]] > 0:
                        count[s[begin]] -= 1
                        begin += 1
                    if len(res) == 0 or len(s) > end - begin:
                        res = s[begin:end]
                continue
            if s[end] == s[begin]:
                begin += 1
                end += 1
                while count[s[begin]] > 0:
                    count[s[begin]] -= 1
                    begin += 1
            else:
                count[s[end]] += 1
                end += 1
            if len(res) == 0 or len(res) > end - begin:
                res = s[begin:end]
        return res
        
# @lc code=end

print(Solution().minWindow("cabefgecdaecf", "cae"))
