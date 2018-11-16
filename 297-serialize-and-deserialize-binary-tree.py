"""
Problem Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a
binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serializeHelper(root, string):
            if root is None:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = serializeHelper(root.left, string)
                string = serializeHelper(root.right, string)
            return string
        return serializeHelper(root,"")


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserializeHeper(l):
            if l[0] == "None":
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = deserializeHeper(l)
            root.right = deserializeHeper(l)
            return root
        return deserializeHeper(data.split(','))
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
