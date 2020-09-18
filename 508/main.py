# 508. 出现次数最多的子树元素和
#
# 20200918
# huao

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        sumList = self.sol(root)
        sumDic = {}
        for num in sumList:
            if num in sumDic.keys():
                sumDic[num] += 1
            else:
                sumDic[num] = 1

        maxFreqNum = []
        maxFreq = 0
        for num in sumDic.keys():
            if sumDic[num] > maxFreq:
                maxFreqNum = [num]
                maxFreq = sumDic[num]
            elif sumDic[num] == maxFreq:
                maxFreqNum.append(num)
        return maxFreqNum

    def sol(self, root: TreeNode):
        if root == None:
            return []
        else:
            l = self.sol(root.left)
            r = self.sol(root.right)
            if l == [] and r == []:
                return [root.val]
            elif l == []:
                return [root.val+r[0]] + r
            elif r == []:
                return [root.val+l[0]] + l
            else:
                return [root.val+l[0]+r[0]] + r + l
