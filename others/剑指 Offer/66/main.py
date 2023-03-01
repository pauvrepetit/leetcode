from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # 保存中间状态嘛
        left = [1]
        for i in a:
            left.append(left[-1] * i)
        right = [1]
        for i in a[::-1]:
            right.append(right[-1] * i)
        return [left[i] * right[len(a)-i-1] for i in range(len(a))]
    
print(Solution().constructArr([1,2,3,4,5]))
