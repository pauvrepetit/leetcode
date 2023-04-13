#
# @lc app=leetcode.cn id=2287 lang=python3
#
# [2287] 重排字符形成目标字符串
#

# @lc code=start
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count = dict()
        for c in s:
            if c in count.keys():
                count[c] += 1
            else:
                count[c] = 1
        count_target = dict()
        for c in target:
            if c in count_target.keys():
                count_target[c] += 1
            else:
                count_target[c] = 1
        max_count = 0xFFFFFFF
        for c in count_target.keys():
            if c not in count.keys():
                return 0
            max_count = min(count[c] // count_target[c], max_count)
        return max_count
# @lc code=end

print(Solution().rearrangeCharacters(s = "ilovecodingonleetcode", target = "code"))
print(Solution().rearrangeCharacters(s = "abcba", target = "abc"))
print(Solution().rearrangeCharacters(s = "abbaccaddaeea", target = "aaaaa"))
