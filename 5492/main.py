# 5492. 分割字符串的方案数
# 双周赛No.34
#
# 20200905
# huao


class Solution:
    def numWays(self, s: str) -> int:
        countOne = s.count('1')
        if countOne % 3 != 0:
            return 0
        if countOne == 0:
            return (len(s)-1) * (len(s)-2) // 2 % 1000000007
        count = 0
        zeroList = []
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            if count == countOne // 3:
                countZero = 0
                for j in range(i+1, len(s)):
                    if s[j] == '0':
                        countZero += 1
                    else:
                        break
                zeroList.append(countZero)
                count = 0
                if len(zeroList) == 2:
                    break
        return (zeroList[0]+1) * (zeroList[1]+1) % 1000000007


print(Solution().numWays("10101"))
print(Solution().numWays("1001"))
print(Solution().numWays("0000"))
print(Solution().numWays("100100010100110"))
