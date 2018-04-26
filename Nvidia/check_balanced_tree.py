

def isBalancedTree(root):

    self.isbalanced = True

    def isBalancedTreeHelper(root):
        if not root:
            return 0
        left = 1 + isBalancedTreeHelper(root.left)
        right = 1 + isBalancedTreeHelper(root.right)
        if abs(left - right) > 1:
            self.isbalanced = False
        return max(left, right)

    isBalancedTreeHelper(root)
    return self.isbalanced
