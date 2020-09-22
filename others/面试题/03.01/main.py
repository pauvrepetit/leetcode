# 面试题 03.01. 三合一
#
# 20200922
# huao

class TripleInOne:
    def __init__(self, stackSize: int):
        self.stack = [0 for i in range(stackSize * 3)]
        self.stackTop = [0, 1, 2]
        self.stackSize = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if self.stackTop[stackNum] // 3 < self.stackSize:
            self.stack[self.stackTop[stackNum]] = value
            self.stackTop[stackNum] += 3

    def pop(self, stackNum: int) -> int:
        if self.stackTop[stackNum] == stackNum:
            return -1
        self.stackTop[stackNum] -= 3
        num = self.stack[self.stackTop[stackNum]]
        return num

    def peek(self, stackNum: int) -> int:
        if self.stackTop[stackNum] == stackNum:
            return -1
        return self.stack[self.stackTop[stackNum]-3]

    def isEmpty(self, stackNum: int) -> bool:
        return self.stackTop[stackNum] == stackNum


# Your TripleInOne object will be instantiated and called as such:
obj = TripleInOne(1)
obj.push(0, 1)
obj.push(0, 2)
param_2 = obj.pop(0)
param_3 = obj.pop(0)
param_4 = obj.pop(0)
param_5 = obj.isEmpty(0)
