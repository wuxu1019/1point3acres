"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

"""

class Solution(object):

    def lengthOfLongestSubstringKDistinct_1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        rt = 0
        found = [0] * 256
        for r in range(len(s)):
            found[ord(s[r])] += 1
            while sum(i > 0 for i in found) > k:
                found[ord(s[l])] -= 1
                l += 1
            rt = max(r - l + 1, rt)
        return rt

    def lengthOfLongestSubstringKDistinct_trick(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        record = {}
        rt = 0
        low = 0
        for i, v in enumerate(s):
            record[v] = i
            if len(record) > k:
                low = min(record.values())
                del record[s[low]]
                low += 1
            rt = max(rt, i-low+1)
        return rt

