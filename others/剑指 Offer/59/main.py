from queue import Queue

class MaxQueue:

    def __init__(self):
        self.queue = Queue()
        self.data = []
        self.max_loc = -1


    def max_value(self) -> int:
        if self.queue.empty():
            return -1
        return self.data[self.max_loc]
        

    def push_back(self, value: int) -> None:
        is_empty = self.queue.empty()
        self.queue.put(value)
        self.data.append(value)
        if is_empty or value > self.data[self.max_loc]:
            self.max_loc = len(self.data) - 1


    def pop_front(self) -> int:
        if self.queue.empty():
            return -1
        value = self.queue.get()
        if value != self.data[self.max_loc]:
            return value
        if self.queue.empty():
            self.max_loc = -1
        else:
            self.max_loc = self.max_loc + 1
            for i in range(self.max_loc+1, len(self.data)):
                if self.data[self.max_loc] < self.data[i]:
                    self.max_loc = i
        return value

q = MaxQueue()
q.push_back(1)
q.push_back(2)
q.push_back(2)
print(q.max_value())
q.pop_front()
q.pop_front()
print(q.max_value())
