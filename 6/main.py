# 6. Z 字形变换
#
# 20200721
# huao
#
# 关键在于确定保存转换过程中的那个矩阵的大小，虽然我确定的很粗糙
# 可以把中间的每列一个元素的部分压缩在一起，对输出结果没有影响，可以减少内存使用(虽然对python似乎没有太大的影响

import numpy as np


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= 3:
            numColumns = (int)(len(s) / (numRows - 2)) + 1
        else:
            numColumns = len(s) * 2
        matrix = np.zeros([numRows, numColumns], dtype=int, order='F')
        i = 0
        for column in range(numColumns):
            if column % 2 == 0:
                # 第1、3、5...列
                for row in range(numRows):
                    if i >= len(s):
                        break
                    matrix[row][column] = ord(s[i])
                    i = i + 1
            else:
                # 第2、4、6...列
                for row in range(1, numRows - 1)[::-1]:
                    if i >= len(s):
                        break
                    matrix[row][column] = ord(s[i])
                    i = i + 1
            if i >= len(s):
                break
        s_result = ""
        print(matrix)
        for row in range(numRows):
            for column in range(numColumns):
                if matrix[row][column] == 0:
                    continue
                s_result = s_result + chr(matrix[row][column])
        return s_result


sol = Solution()
print(sol.convert("AB", 1))
print(sol.convert("LEETCODEISHIRING", 4))
