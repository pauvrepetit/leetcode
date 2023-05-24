from typing import List
#
# @lc app=leetcode.cn id=1377 lang=python3
#
# [1377] T 秒后青蛙的位置
#

# @lc code=start
import queue

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        tree = dict()
        tree[0] = [1]
        tree[1] = [0]
        for a, b in edges:
            if a in tree.keys():
                tree[a].append(b)
            else:
                tree[a] = [b]
            if b in tree.keys():
                tree[b].append(a)
            else:
                tree[b] = [a]
        visited = [False for _ in range(n+1)]
        prop = [0.0 for _ in range(n+1)]
        depth = [0 for _ in range(n+1)]
        frontier = queue.Queue()
        frontier.put(1)
        visited[0] = True
        visited[1] = True
        prop[1] = 1
        while not frontier.empty():
            node = frontier.get()
            flag = True
            for adj in tree[node]:
                if not visited[adj]:
                    flag = False
                    frontier.put(adj)
                    visited[adj] = True
                    depth[adj] = depth[node] + 1
                    prop[adj] = prop[node] / (len(tree[node]) - 1)
            if flag:
                depth[node] += 0xF000000
        if depth[target] == t:
            return prop[target]
        if depth[target] >= 0xF000000 and depth[target] - 0xF000000 <= t:
            return prop[target]
        return 0

# @lc code=end

print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4))
print(Solution().frogPosition(1, [], 1, 1))