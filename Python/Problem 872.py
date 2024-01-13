# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def get_leaf_node_values(self, node, leaf_values):
        if not node.left and not node.right:
            leaf_values.append(node.val)
        if node.left:
            self.get_leaf_node_values(node.left, leaf_values)
        if node.right:
            self.get_leaf_node_values(node.right, leaf_values)

    def leafSimilar(self, root1, root2):
        leaf_tree1, leaf_tree2 = [], []
        self.get_leaf_node_values(root1, leaf_tree1)
        self.get_leaf_node_values(root2, leaf_tree2)
        return leaf_tree1 == leaf_tree2
# Driver Code
if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(0)

    solution = Solution()
    if solution.leafSimilar(root1, root2):
        print("Same")
    else:
        print("Not Same")