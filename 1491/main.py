# 1491. 去掉最低工资和最高工资后的工资平均值
#
# 20200728
# huao
# 求和 找最大/最小值 平均

class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = 10 ** 6
        maxSalary = 10 ** 3
        sumSalary = 0
        for i in salary:
            minSalary = min(minSalary, i)
            maxSalary = max(maxSalary, i)
            sumSalary += i
        return (sumSalary - minSalary - maxSalary) / (len(salary) - 2)
