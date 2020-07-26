# 1028. 从先序遍历还原二叉树
#
# 20200726
# huao
# 用带条件的先序遍历还原二叉树
# 递归
# 把先序遍历分成两个子树部分，分别生成即可

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if S == "":
            return None
        depth = 0
        for i in S:
            if i == '-':
                depth += 1
            if i != '-':
                break
        numLen = 0
        num = 0
        for i in range(len(S))[depth:]:
            if S[i] == '-':
                break
            else:
                num *= 10
                num += int(S[i])
                numLen += 1
        root = TreeNode(num)

        depthStr = ""
        for i in range(depth + 1):
            depthStr += "-"
        mid = -1
        for i in range(len(S) - depth - depth - 1 - numLen):
            i = i + depth + numLen + depth + 1
            if S[i:].startswith(depthStr) and S[i + depth + 1] != '-' and S[i - 1] != '-':
                mid = i
                break

        if mid == -1:
            root.left = self.recoverFromPreorder(S[depth+numLen:])
            root.right = None
        else:
            root.left = self.recoverFromPreorder(S[depth+numLen:mid])
            root.right = self.recoverFromPreorder(S[mid:])
        return root


sol = Solution()
print(sol.recoverFromPreorder("1-401--349---90--88"))
