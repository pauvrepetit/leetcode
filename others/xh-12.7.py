# xh-12.7. 树上最接近的两部分
#
# 20200802
# huao
# 求总和 以及 以每个节点为根的子树的和
# 切开一条边的结果就是 以该边下面的那个节点为根结点的树 和 另外的一部分
# 那么有了总和 和该子树的和 两部分的和就都知道了
# 遍历所有节点 求一个最小值就行
# 需要注意的是，根结点不行 因为没有边指向根结点

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def similarTwoParts(self, root: TreeNode) -> int:
        sumList = []
        sum = self.subTreeSum(root, sumList)
        minSub = 0
        flag = 0
        length = len(sumList)
        for num in sumList[:length-1]:
            sub = num - (sum - num)
            if sub < 0:
                sub = -sub
            if flag == 0:
                flag = 1
                minSub = sub
            else:
                minSub = min(minSub, sub)
        return minSub

    def subTreeSum(self, root: TreeNode, sumList: List[int]) -> int:
        if root == None:
            return 0
        leftSum = self.subTreeSum(root.left, sumList)
        rightSum = self.subTreeSum(root.right, sumList)
        nowSum = leftSum + rightSum + root.val
        sumList.append(nowSum)
        return nowSum


sol = Solution()
node1 = TreeNode(3)
node2 = TreeNode(-1)
node1.left = node2
print(sol.similarTwoParts(node1))
