from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 1:
            return True
        mid = postorder[-1]
        mid_index = -1
        flag = False
        for i in range(len(postorder)-1):
            if not flag and postorder[i] > mid:
                mid_index = i
                flag = True
            if flag and postorder[i] < mid:
                return False
        return self.verifyPostorder(postorder[:mid_index]) and self.verifyPostorder(postorder[mid_index:-1])

print(Solution().verifyPostorder([1,2,5,10,6,9,4,3]))
