from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        left = [0]
        right = graph[0]
        see = [0 for i in range(len(graph))]
        see[0] = 1
        count = 1
        while count < len(graph):
            beforeCount = count
            for v in right:
                if see[v] == 0:
                    for i in graph[v]:
                        if i in right:
                            return False
                    left += graph[v]
                    count += 1
                    see[v] = 1
            for v in left:
                if see[v] == 0:
                    for i in graph[v]:
                        if i in left:
                            return False
                    right += graph[v]
                    count += 1
                    see[v] = 1
            if beforeCount == count:
                for i in range(len(graph)):
                    if see[i] == 0:
                        left.append(i)
                        right += graph[i]
                        count += 1
                        see[i] = 1
                        break
        return True


print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
print(Solution().isBipartite([[3], [2, 4], [1], [0, 4], [1, 3]]))
print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
