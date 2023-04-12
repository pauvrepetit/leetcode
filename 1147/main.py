#
# @lc app=leetcode.cn id=1147 lang=python3
#
# [1147] 段式回文
#

# @lc code=start
class Solution:
    def longestDecomposition(self, text: str) -> int:
        if text == '':
            return 0
        for i in range(1, len(text) // 2 + 1):
            if text[:i] == text[len(text)-i:]:
                return self.longestDecomposition(text[i:len(text)-i]) + 2
        return 1

# @lc code=end

print(Solution().longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
print(Solution().longestDecomposition("merchant"))
print(Solution().longestDecomposition("antaprezatepzapreanta"))
print(Solution().longestDecomposition("elvtoelvto"))

# 这就是个贪心的操作（虽然是个hard的题目）
# 边界的问题
