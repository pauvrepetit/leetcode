# 1566. 重复至少 K 次且长度为 M 的模式
# 周赛No.204
# 
# 20200905
# huao

from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m * k + 1):
            pattern = arr[i:i+m]
            if pattern * k == arr[i:i+m*k]:
                return True
        return False


print(Solution().containsPattern([2, 2], 1, 2))
print(Solution().containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3))
print(Solution().containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
print(Solution().containsPattern(arr=[1, 2, 1, 2, 1, 3], m=2, k=3))
print(Solution().containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2))
print(Solution().containsPattern(arr=[2, 2, 2, 2], m=2, k=3))
