"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:
Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
Note: All the values of tree nodes are in the range of [-1e7, 1e7].


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return max(self.get_max(root))

    def get_max(self, root):
        """Return max increasing and max decreasing ending at root, and max overall."""
        if not root:
            return 0, 0, 0

        inc, dec = 1, 1

        li, ld, lt = self.get_max(root.left)
        ri, rd, rt = self.get_max(root.right)

        if root.left:
            if li and root.left.val - root.val == 1:
                inc = li + 1

            if ld and root.left.val - root.val == -1:
                dec = ld + 1

        if root.right:
            if ri and root.right.val - root.val == 1:
                inc = max(inc, ri + 1)

            if rd and root.right.val - root.val == -1:
                dec = max(dec, rd + 1)

        return inc, dec, max(inc + dec - 1, lt, rt)