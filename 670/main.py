# 670. 最大交换
#
# 20200905
# huao

class Solution:
    def maximumSwap(self, num: int) -> int:
        return int(self.maximumSwapStr(str(num)))

    def maximumSwapStr(self, num: str) -> str:
        s = list(num)
        if len(s) == 1:
            return num
        maxNum = '0'
        maxLoc = 0
        for i in range(len(s))[::-1]:
            c = s[i]
            if maxNum < c:
                maxNum = c
                maxLoc = i
        if s[0] == maxNum:
            return maxNum + self.maximumSwapStr(num[1:])
        s[maxLoc] = s[0]
        s[0] = str(maxNum)
        ss = ""
        for i in s:
            ss += i
        return ss


print(Solution().maximumSwap(100))
print(Solution().maximumSwap(2736))
print(Solution().maximumSwap(9973))
print(Solution().maximumSwap(98638))
