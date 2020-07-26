# 227. 基本计算器 II
#
# 20200726
# huao
# 包含加减乘除，不包含括号的算式的计算
# 还是编译原理中讲过的那些思想
# 归约

class Solution:
    def calculate(self, s: str) -> int:
        equation = []
        i = 0
        while i < len(s):
            if s[i] in ['+', '-', '*', '/']:
                equation.append(s[i])
                i += 1
                continue
            elif s[i] == ' ':
                i += 1
                continue
            else:
                num = 0
                while i < len(s) and s[i] not in ['+', '-', '*', '/', ' ']:
                    num *= 10
                    num += int(s[i])
                    i += 1
                if len(equation) == 0:
                    equation.append(num)
                elif equation[len(equation) - 1] == '*':
                    equation.pop()
                    equation.append(equation.pop() * num)
                elif equation[len(equation) - 1] == '/':
                    equation.pop()
                    equation.append(equation.pop() // num)
                else:
                    equation.append(num)
        stack = []
        for i in equation:
            if i in ['+', '-']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    stack.append(i)
                elif stack[len(stack) - 1] == '+':
                    stack.pop()
                    stack.append(stack.pop() + i)
                else:
                    stack.pop()
                    stack.append(stack.pop() - i)
        return stack[0]


sol = Solution()
print(sol.calculate("0-0"))
