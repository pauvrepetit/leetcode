# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "null"
        # return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        queue = [root]
        res = ""
        index = 0
        while index != len(queue):
            node = queue[index]
            if node != None:
                res += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += "null"
            res += ","
            index += 1
        return res[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "null":
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = [root]
        index = 0
        node_index = 1
        while node_index < len(nodes):
            if nodes[node_index] == "null":
                queue[index].left = None
            else:
                queue[index].left = TreeNode(int(nodes[node_index]))
                queue.append(queue[index].left)
            node_index += 1
            if nodes[node_index] == "null":
                queue[index].right = None
            else:
                queue[index].right = TreeNode(int(nodes[node_index]))
                queue.append(queue[index].right)
            node_index += 1
            index += 1
        return root
        


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
c.left = d
c.right = e

ser = Codec().serialize(a)
print(ser)
Codec().deserialize(ser)
