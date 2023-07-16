import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 大顶堆的最大值要小于小顶堆的最小值
        self.big_heap = []
        self.small_heap = []


    def addNum(self, num: int) -> None:
        if len(self.big_heap) == 0 and len(self.small_heap) == 0:
            heapq.heappush(self.big_heap, -num)
        elif len(self.big_heap) == 1 and len(self.small_heap) == 0:
            val = -heapq.heappop(self.big_heap)
            heapq.heappush(self.big_heap, -min(num, val))
            heapq.heappush(self.small_heap, max(num, val))
        else:
            big_heap_big = -heapq.heappop(self.big_heap)
            heapq.heappush(self.big_heap, -big_heap_big)
            small_heap_small = heapq.heappop(self.small_heap)
            heapq.heappush(self.small_heap, small_heap_small)
            if num < small_heap_small:
                heapq.heappush(self.big_heap, -num)
            else:
                heapq.heappush(self.small_heap, num)
            
            big_len = len(self.big_heap)
            small_len = len(self.small_heap)
            if big_len == small_len:
                return
            if big_len < small_len:
                val = heapq.heappop(self.small_heap)
                heapq.heappush(self.big_heap, -val)
            elif big_len == small_len + 2:
                val = -heapq.heappop(self.big_heap)
                heapq.heappush(self.small_heap, val)


    def findMedian(self) -> float:
        if len(self.big_heap) == 0:
            return 0
        if len(self.big_heap) == len(self.small_heap):
            big = -heapq.heappop(self.big_heap)
            small = heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap, -big)
            heapq.heappush(self.small_heap, small)
            return (big + small) / 2
        big = -heapq.heappop(self.big_heap)
        heapq.heappush(self.big_heap, -big)
        return big



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())
obj.addNum(-1)
print(obj.findMedian())
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(-3)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())