# 5512. 统计不开心的朋友
# 周赛No.206
#
# 20200913
# huao

from typing import List


def compare(preferences: List[List[int]], x: int, u: int, y: int) -> bool:
    preference = preferences[x]
    for i in preference:
        if i == u:
            return True
        elif i == y:
            return False


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        unhappy = set([])
        for i in range(n // 2):
            for j in range(n // 2):
                if i == j:
                    continue
                # pairs[i] and pairs[j]
                x = pairs[i][0]
                y = pairs[i][1]
                u = pairs[j][0]
                v = pairs[j][1]
                if compare(preferences, x, u, y) and compare(preferences, u, x, v):
                    unhappy.add(x)
                else:
                    u = pairs[j][1]
                    v = pairs[j][0]
                    if compare(preferences, x, u, y) and compare(preferences, u, x, v):
                        unhappy.add(x)

                x = pairs[i][1]
                y = pairs[i][0]
                u = pairs[j][0]
                v = pairs[j][1]
                if compare(preferences, x, u, y) and compare(preferences, u, x, v):
                    unhappy.add(x)
                else:
                    u = pairs[j][1]
                    v = pairs[j][0]
                    if compare(preferences, x, u, y) and compare(preferences, u, x, v):
                        unhappy.add(x)
        return len(unhappy)


print(Solution().unhappyFriends(6,
                                [[2, 1, 4, 5, 3], [4, 0, 3, 2, 5], [3, 0, 4, 1, 5], [
                                    2, 4, 5, 0, 1], [5, 1, 2, 3, 0], [2, 0, 3, 1, 4]],
                                [[0, 5], [4, 3], [2, 1]]))
