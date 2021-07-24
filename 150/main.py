# 150. 逆波兰表达式求值
#
# 20210724
# huao

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"
        stack = []
        for token in tokens:
            if token in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(str(int(eval(num1 + token + num2))))
            else:
                stack.append(token)
        return int(stack[0])
