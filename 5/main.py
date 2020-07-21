# 5. 最长回文子串
#
# 20200720
# huao
#
# 这样写算是穷举了，O(n^2)

from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLen = len(s)
        maxSubStr = ""
        for i in range(strLen):
            for j in range(i + 1, strLen + 1):
                if i == 0:
                    if s[i:j] == s[j - 1::-1] and j - i > len(maxSubStr):
                        maxSubStr = s[i:j]
                elif s[i:j] == s[j - 1:i - 1:-1] and j - i > len(maxSubStr):
                    maxSubStr = s[i:j]
        return maxSubStr


sol = Solution()
print(sol.longestPalindrome("aba"))
