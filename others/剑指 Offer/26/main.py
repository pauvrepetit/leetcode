class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSub(self, A: TreeNode, B: TreeNode) -> bool:
        if A == None or B == None:
            return False
        if A.val == B.val:
            flag1 = False
            if B.left == None:
                flag1 = True
            elif A.left != None and B.left != None:
                flag1 = self.isSub(A.left, B.left)
            flag2 = False
            if B.right == None:
                flag2 = True
            elif A.right != None and B.right != None:
                flag2 = self.isSub(A.right, B.right)
            if flag1 and flag2:
                return True
        return False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A == None:
            return False
        if self.isSub(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
a.right = c
b.left = d
t = TreeNode(3)
print(Solution().isSubStructure(a, t))
