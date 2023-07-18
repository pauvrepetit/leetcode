#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.queue = []
        self.htable = dict()
        self.begin = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.htable.keys() and self.htable[key] >= self.begin:
            index = self.htable[key]
            value = self.queue[index]
            self.queue[index] = None
            self.queue.append(value)
            self.htable[key] = len(self.queue) - 1
            while self.queue[self.begin] == None:
                self.begin += 1
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.htable.keys() and self.htable[key] >= self.begin:
            index = self.htable[key]
            self.queue[index] = None
            self.queue.append(value)
            self.htable[key] = len(self.queue) - 1
        else:
            self.queue.append(value)
            self.htable[key] = len(self.queue) - 1
            if len(self.htable.keys()) > self.capacity:
                self.begin += 1
        while self.queue[self.begin] == None:
            self.begin += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

obj = LRUCache(2)
obj.put(2, 1)
obj.put(1, 1)
# print(obj.get(2))
obj.put(2, 3)
# print(obj.get(2))
obj.put(4, 1)
print(obj.get(1))
print(obj.get(2))
# print(obj.get(3))
# print(obj.get(4))
