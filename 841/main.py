# 841. 钥匙和房间
#
# 20200831
# huao
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        roomNum = len(rooms)
        lockCount = roomNum - 1
        lock = [1 for i in range(roomNum)]
        lock[0] = 0

        while True:
            lockCount_ = lockCount
            for i in range(roomNum):
                if lock[i] == 0:
                    for j in rooms[i]:
                        if lock[j] == 1:
                            lock[j] = 0
                            lockCount -= 1
            if lockCount == lockCount_:
                break
        if lockCount == 0:
            return True
        else:
            return False


print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
