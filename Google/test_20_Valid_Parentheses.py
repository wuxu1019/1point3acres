"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
"""


class Solution(object):
    def isValid_2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2:
            return False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')

        return s == ''

    def isValid_1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        mp = {'}': '{', ']': '[', ')': '('}
        left = '{[('
        for c in s:
            if c in left:
                stk.append(c)
            else:
                if not stk or stk[-1] != mp[c]:
                    return False
                stk.pop()
        return len(stk) == 0
