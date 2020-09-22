# 968. 监控二叉树
#
# 20200922
# huao
# 我自己都想像不到，这个题就这样过了???
# 贪心，从叶子结点开始贪心

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        newRoot = TreeNode(0)
        newRoot.left = root
        return self.sol(newRoot)[0]

    # 返回监视树root的非根节点需要的摄像机的数量，以及此时根节点处是否有摄像机，此时根节点是否被监视
    def sol(self, root: TreeNode):
        if root == None:
            return 0, False, True
        leftCameraCount, leftCamera, leftSee = self.sol(root.left)
        rightCameraCount, rightCamera, rightSee = self.sol(root.right)
        if leftCamera and rightCamera:
            return leftCameraCount+rightCameraCount, False, True
        elif leftCamera and not rightCamera:
            if rightSee:
                return leftCameraCount+rightCameraCount, False, True
            else:
                return leftCameraCount+rightCameraCount+1, True, True
        elif not leftCamera and rightCamera:
            if leftSee:
                return leftCameraCount+rightCameraCount, False, True
            else:
                return leftCameraCount+rightCameraCount+1, True, True
        else:
            if leftSee and rightSee:
                return leftCameraCount+rightCameraCount, False, False
            else:
                return leftCameraCount+rightCameraCount+1, True, True
