import re
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[int]) -> str:
        if len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            i = i + 1
            not_match = 0
            preStr = strs[0][0:i]
            re_preStr = '^' + preStr
            for str1 in strs:
                match = re.search(re_preStr, str1)
                if match == None:
                    not_match = 1
                    break
            if not_match == 1:
                return preStr[0:-1]
        return strs[0]


sol = Solution()
print(sol.longestCommonPrefix(['flower', 'flow', 'flight']))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
print(sol.longestCommonPrefix([]))
print(sol.longestCommonPrefix(['a', 'b']))
