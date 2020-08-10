# 1221. 分割平衡字符串
#
# 20200810
# huao

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        LCount = 0
        RCount = 0
        splitCount = 0
        for c in s:
            if c == 'L':
                LCount += 1
            if c == 'R':
                RCount += 1
            if LCount == RCount:
                splitCount += 1
                LCount = 0
                RCount = 0
        return splitCount


sol = Solution()
print(sol.balancedStringSplit("LLLLRRRR"))
