class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(':
                stack.append('(')
            elif i == '[':
                stack.append('[')
            elif i == '{':
                stack.append('{')
            elif i == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif i == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            else:
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        return False

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("]"))
