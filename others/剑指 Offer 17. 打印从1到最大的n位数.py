# 剑指 Offer 17. 打印从1到最大的n位数
#
# 20200802
# huao
# ......

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1, 10 ** n)]
