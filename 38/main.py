# 38. 外观数列
#
# 20200724
# huao
# 就是个统计罢了


class Solution:
    def countAndSay(self, n: int) -> str:
        countStr = "1"
        for i in range(n - 1):
            nowChar = "-"
            nowCount = 0
            str1 = ""
            for j in countStr:
                if nowChar != j:
                    if nowChar != '-':
                        str1 += str(nowCount) + nowChar
                    nowChar = j
                    nowCount = 1
                else:
                    nowCount += 1
            str1 += str(nowCount) + nowChar
            countStr = str1
        return countStr


sol = Solution()
print(sol.countAndSay(1))
