# 119. 杨辉三角 II
#
# 20200811
# huao
# 怎么说呢，这时间复杂度确实是O(n)，可是交上去测试的结果还比不了别人直接按杨辉三角的方法来求快...

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowNum = [1]
        for i in range(rowIndex):
            rowNum.append(rowNum[i] * (rowIndex-i) // (i+1))
        return rowNum
