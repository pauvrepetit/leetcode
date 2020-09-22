# 面试题 03.02. 栈的最小值
#
# 20200811
# huao
# 我怕是有点傻，另外维护一个栈，保存该位置为栈顶时的最小值就ok了

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataStack = []
        self.minStack = []
        self.stackLength = 0

    def push(self, x: int) -> None:
        self.dataStack.append(x)
        if self.stackLength == 0:
            self.minStack.append(x)
        else:
            self.minStack.append(min(x, self.minStack[self.stackLength-1]))
        self.stackLength += 1

    def pop(self) -> None:
        self.stackLength -= 1
        self.dataStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.dataStack[self.stackLength-1]

    def getMin(self) -> int:
        return self.minStack[self.stackLength-1]
