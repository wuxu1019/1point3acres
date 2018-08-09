"""
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:
s = "aabbcc", k = 3

Result: "abcabc"

The same letters are at least distance 3 from each other.
Example 2:
s = "aaabc", k = 3

Answer: ""

It is not possible to rearrange the string.
Example 3:
s = "aaadbbcc", k = 2

Answer: "abacabcd"

Another possible answer is: "abcabcda"

The same letters are at least distance 2 from each other.
Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.
"""


class Solution(object):
    def rearrangeString_priorityQ(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        ct = collections.Counter(s)
        data = [(-v, n) for n, v in ct.items()]
        groups = []

        while data:

            heapq.heapify(data)
            stk = []
            for _ in range(k):
                if len(groups) == len(s):
                    return ''.join(groups)
                if not data:
                    return ''
                freq, c = heapq.heappop(data)
                groups += c
                if freq < -1:
                    stk.append((freq + 1, c))
            data += stk

        return ''.join(groups)

    def rearrangeString_sort(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        ct = collections.Counter(s)
        data = [[n, v] for v, n in ct.items()]

        rt, j = [''] * len(s), 0
        while j < len(s):
            data.sort(reverse=1)
            for i in range(k):
                if j == len(s):
                    return ''.join(rt)
                elif i >= len(data) or data[i][0] == 0:
                    return ''
                rt[j] = data[i][1]
                data[i][0] -= 1
                j += 1
        return ''.join(rt)
