# 685. 冗余连接 II
#
# 20200917
# huao

from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        nodeFather = [i for i in range(len(edges)+1)]
        errEdge = None
        errEdge2 = None
        for edge in edges:
            source, target = edge
            if nodeFather[target] != target and nodeFather[target] != source:
                errEdge = edge
            elif self.checkFather(nodeFather, source, target):
                nodeFather[target] = source
            else:
                errEdge2 = edge

        if errEdge == None:
            return errEdge2
        if self.checkFather(nodeFather, errEdge[0], errEdge[1]):
            return [nodeFather[errEdge[1]], errEdge[1]]
        else:
            return errEdge

    def checkFather(self, nodeFather: List[int], source: int, target: int) -> bool:
        return self.getFather(nodeFather, source) != self.getFather(nodeFather, target)

    def getFather(self, nodeFather: List[int], node: int) -> int:
        while nodeFather[node] != node:
            node = nodeFather[node]
        return node


print(Solution().findRedundantDirectedConnection(
    [[2, 1], [4, 2], [1, 4], [3, 1]]))
