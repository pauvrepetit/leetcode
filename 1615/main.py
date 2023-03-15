from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [[i, 0] for i in range(n)]
        csr = [[] for _ in range(n)]
        for a, b in roads:
            degrees[a][1] += 1
            degrees[b][1] += 1
            csr[a].append(b)
            csr[b].append(a)
        degrees.sort(key=lambda x:x[1], reverse=True)

        if degrees[0][1] != degrees[1][1]:
            # 如果最大度数和次大度数不相等，那么最大度数的点是一定要选的，然后从次大度数的点里面选一个就ok
            max_rank = degrees[0][1] + degrees[1][1] - 1
            for id, degree in degrees[1:]:
                if degree == degrees[1][1] and degrees[0][0] not in csr[id]:
                    return max_rank + 1
                if degree != degrees[1][1]:
                    break
            return max_rank
        else:
            # 如果最大度数和次大度数相等，那么就需要在最大度数里面选两个，这个就得全部遍历一遍了
            ids = []
            max_degree = degrees[0][1]
            for id, degree in degrees:
                if degree == max_degree:
                    ids.append(id)
                else:
                    break
            max_rank = 2 * max_degree - 1
            for ii in range(len(ids)):
                i = ids[ii]
                for j in ids[ii+1:]:
                    if i not in csr[j]:
                        return max_rank + 1
            return max_rank

print(Solution().maximalNetworkRank(n = 5, roads = [[2,3],[0,3],[0,4],[4,1]]))
print(Solution().maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]))
print(Solution().maximalNetworkRank(n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))
print(Solution().maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))
