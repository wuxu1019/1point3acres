"""
if a tree is valid binary search tree
"""
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isValidBST(root):
    if not root:
        return True

    if root.left and root.val < root.left.val:
        return False
    if root.right and root.val > root.right.val:
        return False

    return isValidBST(root.left) and isValidBST(root.right)


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    rt = isValidBST(root)
    print rt