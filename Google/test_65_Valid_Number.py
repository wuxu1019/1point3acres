"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lstrip(' ')
        s = s.rstrip(' ')
        if not s:
            return False
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        if ' ' in s:
            return False
        if 'e' in s and s.count('e') == 1:
            a, b = s.split('e')
            if b:
                b = b[1:] if b[0] == '+' or b[0] == '-' else b
                if self.isNumberHelper(a) and b.isdigit():
                    return True
        elif 'E' in s and s.count('E') == 1:
            a, b = s.split('E')
            if b:
                b = b[1:] if b[0] == '+' or b[0] == '-' else b
                if self.isNumberHelper(a) and b.isdigit():
                    return True
        elif self.isNumberHelper(s):
            return True

        return False

    def isNumberHelper(self, s):
        if '.' in s and s.count('.') == 1:
            a, b = s.split('.')
            if not a and not b:
                return False
            if (a.isdigit() or not a) and (b.isdigit() or not b):
                return True
        elif '.' not in s and s.isdigit():
            return True
        return False
