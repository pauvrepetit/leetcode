# 1304. 和为零的N个唯一整数
#
# 20200729
# huao
# emmm...

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 1:
            nums = [0]
            for i in range(n // 2):
                nums.append(i + 1)
                nums.append(- i - 1)
            return nums
        else:
            for i in range(n // 2):
                nums.append(i + 1)
                nums.append(- i - 1)
            return nums
