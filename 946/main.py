# 946. 验证栈序列
#
# 20200918
# huao

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while True:
            if stack == [] and pushed == []:
                return True
            if popped == []:
                return False
            if stack == []:
                stack.append(pushed.pop(0))
            else:
                if popped[0] == stack[-1]:
                    popped.pop(0)
                    stack.pop()
                else:
                    if pushed == []:
                        return False
                    stack.append(pushed.pop(0))


print(Solution().validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
