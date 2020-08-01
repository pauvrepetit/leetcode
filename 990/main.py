# 990. 等式方程的可满足性
#
# 20200801
# huao
# 先扫一遍等式 把变量分成若干组 组内相等 组间不确定
# 再扫一遍不等式 如果存在组内两个变量的不等关系 则存在冲突
# 否则就没有问题

from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parts = [[chr(i)] for i in range(ord('a'), ord('z')+1)]
        for equation in equations:
            if equation[1] == '!':
                continue
            num1 = equation[0]
            num2 = equation[3]
            part1 = []
            part2 = []
            for part in parts:
                if part1 == [] and num1 in part:
                    part1 = part
                if part2 == [] and num2 in part:
                    part2 = part
                if part1 != [] and part2 != []:
                    break
            if part1 != part2 and part1 != [] and part2 != []:
                parts.remove(part1)
                parts.remove(part2)
                parts.append(part1 + part2)
        for equation in equations:
            if equation[1] == '=':
                continue
            num1 = equation[0]
            num2 = equation[3]
            for part in parts:
                if num1 in part and num2 in part:
                    return False
        return True


sol = Solution()
print(sol.equationsPossible(["a==b", "b==c", "a==c"]))
