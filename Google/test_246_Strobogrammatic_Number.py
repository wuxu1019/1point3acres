"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false

"""


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        same = '018'
        diff = '69'
        l, r = 0, len(num) - 1
        while l < r:
            s = num[l] + num[r]
            if s[0] in same and s.count(s[0]) == len(s):
                l += 1
                r -= 1
            elif s == diff or s[::-1] == diff:
                l += 1
                r -= 1
            else:
                return False
        if l == r:
            return num[r] in same
        return True
