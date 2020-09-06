# 5494. 统计所有可行路径
# 双周赛No.34
#
# 20200905
# huao

from typing import List

f = [[-1 for i in range(210)] for j in range(210)]


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        for i in range(210):
            for j in range(210):
                f[i][j] = -1
        f[start][0] = 1
        sum = 0
        for i in range(fuel+1):
            sum += self.sol(locations, start, finish, i)
            sum %= 1000000007
        return sum

    def sol(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if abs(locations[start] - locations[finish]) > fuel:
            f[finish][fuel] = 0
            return 0
        if f[finish][fuel] == -1:
            sum = 0
            for k in range(len(locations)):
                if k == finish:
                    continue
                if fuel < abs(locations[finish] - locations[k]):
                    continue
                    # f[k][fuel-abs(locations[finish] - locations[k])] = 0
                elif f[k][fuel-abs(locations[finish] - locations[k])] == -1:
                    f[k][fuel-abs(locations[finish] - locations[k])] = self.sol(
                        locations, start, k, fuel - abs(locations[finish] - locations[k]))
                sum += f[k][fuel-abs(locations[finish] - locations[k])]
                sum %= 1000000007
            f[finish][fuel] = sum
        return f[finish][fuel]


print(Solution().countRoutes([758,891,544,807,851,545,889,577,719,724,538,799,734,798,690,658,877,638,637,743,709,549,730,809,636,567,893,590,944,787,921,878,931,848,987,586,941,702,974,739,909,555,963],16,23,90))
