"""
judge if a tree is a Balanced BST
"""

def isBanlancBST(root):

    def isBanlancBSTHelper(root):
        if not root:
            return 0
        l = isBanlancBSTHelper(root.left)
        r = isBanlancBSTHelper(root.right)
        if l == -1 or r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return 1 + max(l, r)
    if isBanlancBSTHelper(root) == -1:
        return False
    return True


