class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    global isValidBST
    def isValidBST(root:TreeNode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False

            return True
        return helper(root, float('-inf'), float('inf'))

    def test(root): 
        if (isValidBST(root)):
            print ("Is BST")
        else:
            print ("Not a BST")

    # change here
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(7)
        
    test(root)

    # change here
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    test(root)