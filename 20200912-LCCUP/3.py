# LCP 19. 秋叶收藏集
# LeetCode CUP 2020 Fall
#
# 20200912
# huao

import heapq


class P:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.y < other.y

    def __gt__(self, other):
        return self.y > other.y

    def __eq__(self, other):
        return self.y == other.y


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        count = 0
        if leaves[0] == 'y' and leaves[-1] == 'y':
            return 2 + self.sol(leaves[1:-1])
        elif leaves[0] == 'y':
            return 1 + self.sol(leaves[1:].strip('r'))
        elif leaves[-1] == 'y':
            return 1 + self.sol(leaves[:-1].strip('r'))
        else:
            return self.sol(leaves.strip('r'))

    # 保证leaves的左右均为y

    def sol(self, leaves: str) -> int:
        if leaves == "":
            return 1
        countsLeftR = []
        countsRightY = []
        count = 0
        for l in leaves:
            if l == 'r':
                count += 1
            else:
                countsLeftR.append(count)
        count = 0
        for l in leaves[::-1]:
            if l == 'y':
                countsRightY.append(count)
                count += 1
        countsRightY = countsRightY[::-1]

        h = []
        for i in range(len(countsLeftR)):
            heapq.heappush(h, P(i, countsLeftR[i]+countsRightY[i]))

        count = len(leaves)
        for i in range(len(countsLeftR)):
            while len(h) != 0 and h[0].x < i:
                heapq.heappop(h)
            if len(h) != 0:
                count = min(count, h[0].y - countsLeftR[i] + i)
        return count


print(Solution().minimumOperations("yyrryy"))
