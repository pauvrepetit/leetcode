# 118. 杨辉三角
#
# 20200725
# huao
# 这也是很easy的一个题吧
# 要说思想，这可以算是最基本的动态规划吧

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        yanghui = []
        for row in range(numRows):
            yanghuiRow = []
            for column in range(row + 1):
                if column == 0:
                    yanghuiRow.append(1)
                elif column == row:
                    yanghuiRow.append(1)
                else:
                    yanghuiRow.append(
                        yanghui[len(yanghui) - 1][column - 1] + yanghui[len(yanghui) - 1][column])
            yanghui.append(yanghuiRow)
        return yanghui


sol = Solution()
print(sol.generate(5))
