# LCP 03. 机器人大冒险
#
# 20200801
# huao
# 总归是要做一些细节上的优化

from typing import List
from functools import cmp_to_key


def cmp(x: List[int], y: List[int]) -> int:
    if x[0] == y[0]:
        return x[1] - y[1]
    else:
        return x[0] - y[0]


class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        loc = [0, 0]
        obstaclesLen = len(obstacles)
        uTime = command.count('U')
        rTime = command.count('R')
        if obstaclesLen == 0:
            time = min(x // rTime, y // uTime)
            loc[0] = rTime * time
            loc[1] = uTime * time
            while True:
                for c in command:
                    if c == 'U':
                        loc[1] += 1
                    else:
                        loc[0] += 1
                    if loc[0] > x or loc[1] > y:
                        return False
                    if loc == [x, y]:
                        return True
        else:
            # obstacles.sort(key=cmp_to_key(cmp))
            minX = obstacles[0][0]
            minY = obstacles[0][1]
            maxX = obstacles[0][0]
            maxY = obstacles[0][1]
            for xx, yy in obstacles[1:]:
                minX = min(minX, xx)
                maxX = max(maxX, xx)
                minY = min(minY, yy)
                maxY = max(maxY, yy)

            time = min(min(minX, x) // rTime, min(minY, y) // uTime)
            loc[0] = rTime * time
            loc[1] = uTime * time

            while True:
                for c in command:
                    if c == 'U':
                        loc[1] += 1
                    else:
                        loc[0] += 1
                    if loc[0] > x or loc[1] > y:
                        return False
                    if loc == [x, y]:
                        return True
                    if loc[0] >= minX and loc[0] <= maxX and loc[1] >= minY and loc[1] <= maxY:
                        if loc in obstacles:
                            return False
