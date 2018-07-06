"""
count clumps of same color in the tree, here are two clumps below
              R
         R        R
      G   R   B   B
    G
"""

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
count = 0



def CountClumps(root):
    def CountClumpsHelp(root, base):
        global count
        if not root:
            return 0

        ct = CountClumpsHelp(root.left, root.val) + 1 + CountClumpsHelp(root.right, root.val)
        if root.val == base:
            return ct
        if ct >= 2:
            count += 1
        return 0

    CountClumpsHelp(root, None)
    return count

if __name__ == '__main__':
    rt = TreeNode('R')
    rt.left = TreeNode('R')
    rt.right = TreeNode('R')
    rt.left.left = TreeNode('G')
    rt.left.right = TreeNode('R')
    rt.right.left = TreeNode('R')
    rt.right.right = TreeNode('R')
    rt.left.left.left = TreeNode('R')


    ans = CountClumps(rt)
    print ans
