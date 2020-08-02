# 686. 重复叠加字符串匹配
#
# 20200802
# huao
# 如果len(A) >= len(B)，那么就只能是 A 或者 AA
# 如果len(A) < len(B)，那只能是把A扩展到恰好比B长或相等，已经较其再多一个A

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        lenA = len(A)
        lenB = len(B)
        if lenA >= lenB:
            if B in A:
                return 1
            elif B in A+A:
                return 2
            else:
                return -1
        else:
            count = lenB // lenA
            if B in A * count:
                return count
            elif B in A * (count + 1):
                return count + 1
            elif B in A * (count + 2):
                return count + 2
            else:
                return -1
