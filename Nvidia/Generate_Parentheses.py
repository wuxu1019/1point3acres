"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

def generateParenthese(n):
    if n < 1:
        return []

    rt = []
    def generateParentheseHelper(n, l, r, base):
        if l == n and r == n:
            rt.append(base)
        if l < n:
            generateParentheseHelper(n, l+1, r, base+'(')
        if r < l:
            generateParentheseHelper(n, l, r+1, base+')')

    generateParentheseHelper(n, 0, 0, '')
    return rt

if __name__ == '__main__':
    n = 3
    ans = generateParenthese(n)
    print ans


