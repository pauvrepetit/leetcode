from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        res = [[root]]
        level_res = [[root.val]]
        flag = False
        while True:
            prev = res[-1]
            next = []
            next_res = []
            for node in prev[::-1]:
                if flag:
                    if node.left != None:
                        next.append(node.left)
                        next_res.append(node.left.val)
                    if node.right != None:
                        next.append(node.right)
                        next_res.append(node.right.val)
                else:
                    if node.right != None:
                        next.append(node.right)
                        next_res.append(node.right.val)
                    if node.left != None:
                        next.append(node.left)
                        next_res.append(node.left.val)
            flag = not flag
            if len(next) == 0:
                break
            res.append(next)
            level_res.append(next_res)
        return level_res
