# LCP 06. 拿硬币
#
# 20200801
# huao
# 这是不是太简单了...


class Solution:
    def minCount(self, coins: List[int]) -> int:
        count = 0
        for coinNum in coins:
            count += (coinNum + 1) // 2
        return count
