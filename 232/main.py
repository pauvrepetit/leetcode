#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.in_list = []
        self.out_list = []


    def push(self, x: int) -> None:
        self.in_list.append(x)


    def pop(self) -> int:
        if len(self.out_list) != 0:
            return self.out_list.pop()
        in_length = len(self.in_list)
        for _ in range(in_length):
            self.out_list.append(self.in_list.pop())
        return self.out_list.pop()


    def peek(self) -> int:
        if len(self.out_list) != 0:
            return self.out_list[-1]
        in_length = len(self.in_list)
        for _ in range(in_length):
            self.out_list.append(self.in_list.pop())
        return self.out_list[-1]


    def empty(self) -> bool:
        return len(self.in_list) == 0 and len(self.out_list) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

