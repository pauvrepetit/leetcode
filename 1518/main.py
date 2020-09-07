# 1518. 换酒问题
#
# 20200907
# huao

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        num = numBottles
        while numBottles >= numExchange:
            num += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return num


print(Solution().numWaterBottles(numBottles=5, numExchange=5))
print(Solution().numWaterBottles(numBottles=2, numExchange=3))
