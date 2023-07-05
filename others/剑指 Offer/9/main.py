class CQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []


    def appendTail(self, value: int) -> None:
        self.input_stack.append(value)


    def deleteHead(self) -> int:
        if len(self.output_stack) == 0:
            in_len = len(self.input_stack)
            for _ in range(in_len):
                self.output_stack.append(self.input_stack.pop())
        if len(self.output_stack) == 0:
            return -1
        return self.output_stack.pop()
