# 264. 丑数 II
# 剑指 Offer 49. 丑数
#
# 20200801
# huao
# 看来我是真的蠢

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNum = [1]
        i = 0
        j = 0
        k = 0
        t = 1
        while t < n:
            if uglyNum[i] * 2 <= uglyNum[j] * 3 and uglyNum[i] * 2 <= uglyNum[k] * 5:
                if uglyNum[t-1] != uglyNum[i] * 2:
                    uglyNum.append(uglyNum[i] * 2)
                    t += 1
                i += 1
            elif uglyNum[j] * 3 <= uglyNum[i] * 2 and uglyNum[j] * 3 <= uglyNum[k] * 5:
                if uglyNum[t-1] != uglyNum[j] * 3:
                    uglyNum.append(uglyNum[j] * 3)
                    t += 1
                j += 1
            else:
                if uglyNum[t-1] != uglyNum[k] * 5:
                    uglyNum.append(uglyNum[k] * 5)
                    t += 1
                k += 1
        return uglyNum[n-1]


print(Solution().nthUglyNumber(11))
