# 1404. 将二进制表示减到 1 的步骤数
#
# 20200810
# huao
# 统计0和1的数量 和结果之间有着很微妙的关系

class Solution:
    def numSteps(self, s: str) -> int:
        count0 = s.count('0')
        count1 = s.count('1')
        if count1 == 1:
            return count0
        count00 = 0
        for c in s[::-1]:
            if c == '0':
                count00 += 1
            else:
                break
        return count0 + count1 + count0 + 1 - count00


sol = Solution()
print(sol.numSteps("11010"))
