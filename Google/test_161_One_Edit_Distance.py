"""
Given two strings s and t, determine if they are both one edit distance apart.

Note:

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.

"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t) or len(s) == len(t) + 1 or len(t) == len(s) + 1:

            lth = min(len(s), len(t))
            diff = lth
            for i in range(lth):
                if s[i] != t[i]:
                    diff = i
                    break

            if len(s) == len(t):
                return diff != len(s) and s[:diff] + s[diff + 1:] == t[:diff] + t[diff + 1:]
            elif len(s) == len(t) + 1:
                return s[:diff] + s[diff + 1:] == t
            else:
                return t[:diff] + t[diff + 1:] == s
        return False
