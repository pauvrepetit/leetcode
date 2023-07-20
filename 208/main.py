#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = dict()

class Trie:

    def __init__(self):
        self.root = Node("")


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.next.keys():
                node.next[c] = Node("")
            node = node.next[c]
        node.val = word

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.next.keys():
                return False
            node = node.next[c]
        return node.val == word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.next.keys():
                return False
            node = node.next[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

