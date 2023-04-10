from typing import List, Optional

#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        h = head
        length = 0
        data = []
        while h != None:
            length += 1
            data.append(h.val)
            h = h.next
        
        now_max = [i for i in data]
        value = [0 for _ in range(length)]
        for i in range(length-1)[::-1]:
            if data[i] < now_max[i+1]:
                now_max[i] = now_max[i+1]
            else:
                continue

            if data[i] < data[i+1]:
                value[i] = data[i+1]
            elif data[i] == data[i+1]:
                value[i] = value[i+1]
            else:
                for j in range(i+1, length):
                    if data[i] < value[j]:
                        value[i] = value[j]
                        break
                else:
                    value[i] = 0
        return value

# @lc code=end
