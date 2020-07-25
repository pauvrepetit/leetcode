# 224. 基本计算器
#
# 20200725
# huao
# 这个呀 非要说的话 不就是编译中讲过的内容吗
# 移进 归约
# 这个题只有加减法 优先级都是一样的 很容易写的吧

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sLen = len(s)
        i = 0
        while i < sLen:
            if s[i] == '(':
                stack.append('(')
            elif s[i] == '+' or s[i] == '-':
                stack.append(s[i])
            elif s[i] == ' ':
                i += 1
                continue
            elif s[i] == ')':
                num = stack.pop()
                stack.pop()
                if len(stack) == 0:
                    stack.append(num)
                elif stack[len(stack) - 1] == '+':
                    stack.pop()
                    stack.append(stack.pop() + num)
                elif stack[len(stack) - 1] == '-':
                    stack.pop()
                    stack.append(stack.pop() - num)
                else:
                    stack.append(num)
            else:
                # 数字
                num = int(s[i])
                while i < sLen - 1:
                    i += 1
                    if s[i] in ['(', ')', ' ', '+', '-']:
                        i -= 1
                        break
                    else:
                        num = num * 10 + int(s[i])
                # 得到数字num
                if len(stack) == 0:
                    stack.append(num)
                elif stack[len(stack) - 1] == '+':
                    stack.pop()
                    stack.append(stack.pop() + num)
                elif stack[len(stack) - 1] == '-':
                    stack.pop()
                    stack.append(stack.pop() - num)
                else:
                    stack.append(num)
            i += 1
        return stack[0]


sol = Solution()
print(sol.calculate('12 + 13'))
