#!/usr/bin/env python

"""A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
"""


class TreeNode:
    """ Tree Node """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.search(root, root.val)

    def search(self, node, value):
        if not node:
            # empty node
            return True
        
        if node.val != value:
            # current node's value doesn't match provided value
            return False
        
        if self.search(node.left, value) and self.search(node.right, value):
            # child nodes both have same values
            return True

        return False


if __name__ == "__main__":
    sol = Solution()

    tree1 = TreeNode(1)
    tree1.left = TreeNode(1)
    tree1.right = TreeNode(1)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(1)
    tree1.right.right = TreeNode(1)
    print(sol.isUnivalTree(tree1))

    tree2 = TreeNode(2)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(2)
    tree2.left.left = TreeNode(5)
    tree2.left.right = TreeNode(2)
    print(sol.isUnivalTree(tree2))
