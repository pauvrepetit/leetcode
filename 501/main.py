# 501. 二叉搜索树中的众数
#
# 20200924
# huao

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        stack = [root]
        dic = {}
        while stack != []:
            if stack[0].val in dic.keys():
                dic[stack[0].val] += 1
            else:
                dic[stack[0].val] = 1

            if stack[0].left != None:
                stack.append(stack[0].left)
            if stack[0].right != None:
                stack.append(stack[0].right)
            stack.pop(0)
        maxCountNum = []
        maxCount = 0
        for num in dic.keys():
            if dic[num] > maxCount:
                maxCountNum = [num]
                maxCount = dic[num]
            elif dic[num] == maxCount:
                maxCountNum.append(num)
        return maxCountNum


root = TreeNode(1)
left = TreeNode(2)
root.left = left
print(Solution().findMode(root))
