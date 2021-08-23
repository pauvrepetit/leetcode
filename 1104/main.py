# 1104. 二叉树寻路
#
# 20210729
# huao
# 这写的也太丑了，我人都傻了

from typing import List
import math


class Solution:
    def getParent(self, node: int, level: int) -> int:
        offset = node - (1 << level)
        if level % 2 != 0:
            offset = (2 << level) - node - 1
        parent_offset = offset // 2
        parent_level = level - 1
        parent = parent_offset + (1 << parent_level)
        if parent_level % 2 != 0:
            parent = (2 << parent_level) - parent_offset - 1
        return parent

    def pathInZigZagTree(self, label: int) -> List[int]:
        level = int(math.log2(label))
        # level 为 偶数 时，从左向右
        #       为 奇数 时，从右向左
        node = label
        walk = [node]
        while node != 1:
            parent = self.getParent(node, level)
            walk.insert(0, parent)
            node = parent
            level -= 1
        if walk[0] != 1:
            walk.insert(0, 1)
        return walk


print(Solution().pathInZigZagTree(14))
print(Solution().pathInZigZagTree(26))
