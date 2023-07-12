from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) == 0:
            return True
        stack = []
        push_index = 0
        pop_index = 0
        while True:
            if len(stack) != 0 and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
            else:
                if push_index == len(pushed):
                    return False
                stack.append(pushed[push_index])
                push_index += 1
            if push_index == len(pushed) and pop_index == len(popped):
                return True
