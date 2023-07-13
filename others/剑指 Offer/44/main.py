class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        n -= 10
        now_count = 90
        now_index = 10
        now_len = 2
        while True:
            if n < now_count * now_len:
                val = n // now_len + now_index
                offset = n % now_len
                return int(str(val)[offset])
            else:
                n -= now_count * now_len
                now_count *= 10
                now_index *= 10
                now_len += 1
