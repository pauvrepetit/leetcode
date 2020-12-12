# 5611. 石子游戏 VI
# 这是个数学问题，好好算一下，就知道，对于Alice和Bob，他们每次都应该取两人价值和最大的那个石头

from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        data = []
        length = len(aliceValues)
        for i in range(length):
            data.append([aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]])
        
        data.sort(key=lambda x: x[0], reverse=True)
        aliceScore = 0
        bobScore = 0
        for i in range(length):
            if i % 2 == 0:
                aliceScore += data[i][1]
            else:
                bobScore += data[i][2]
        if aliceScore > bobScore:
            return 1
        elif aliceScore == bobScore:
            return 0
        else:
            return -1

print(Solution().stoneGameVI([9,8,3,8], [10,6,9,5]))