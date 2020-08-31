# 605. 种花问题
#
# 20200831
# huao
# 贪心算法

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 1 and n >= 1:
                return False
            elif flowerbed[0] == 0 and n >= 2:
                return False
            else:
                return True
        count = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            count += 1
            flowerbed[0] = 1
        for i in range(len(flowerbed)-1)[1:]:
            if flowerbed[i] == 1:
                continue
            else:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            count += 1
            flowerbed[len(flowerbed)-1] = 1
        return n <= count


print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))
