"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].

"""


class Solution(object):
    def addBoldTag_bruteforce(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        rt = ''
        compress = [False] * len(s)
        for i in range(len(s)):
            for word in dict:
                lth = len(word)
                if s[i:i + lth] == word:
                    compress[i:i + lth] = [True] * lth

        i = 0
        for v, l in itertools.groupby(compress):
            lth = len(list(l))
            if v == True:
                rt += '<b>{0}</b>'.format(s[i:i + lth])
            else:
                rt += '{0}'.format(s[i:i + lth])
            i += lth
        return rt


