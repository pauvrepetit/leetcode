from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        listNum = [a, b, c]
        listNum.sort()
        left = listNum[1] - listNum[0] - 1
        right = listNum[2] - listNum[1] - 1
        if left == 0 and right == 0:
            minMove = 0
        elif 0 in [left, right]:
            minMove = 1
        elif 1 in [left, right]:
            minMove = 1
        else:
            minMove = 2
        maxMove = left + right
        return [int(minMove), int(maxMove)]

sol = Solution()
print(sol.numMovesStones(1, 2, 5))
print(sol.numMovesStones(4, 3, 2))
print(sol.numMovesStones(3, 5, 1))
print(sol.numMovesStones(1, 2, 6))
