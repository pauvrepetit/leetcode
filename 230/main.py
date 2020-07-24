# 230. 二叉搜索树中第K小的元素
#
# 20200724
# huao
# emmm... 这个题呀
# 对二叉搜索树做中根遍历，就得到了有序的数组
# 找第k小也就是O(1)的事情了
# 遍历需要O(n)
# 也不知道能不能在更快的时间内实现呢？

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        orderList = self.midScan(root)
        return orderList[k - 1]

    def midScan(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        orderList = self.midScan(root.left) + [root.val] + self.midScan(root.right)
        return orderList


sol = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node3.left = node1
node3.right = node4
node1.right = node2
print(sol.kthSmallest(node3, 1))
