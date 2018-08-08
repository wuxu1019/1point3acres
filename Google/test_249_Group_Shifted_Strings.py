
"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if not strings:
            return []

        mp = collections.defaultdict(list)

        for s in strings:
            if len(s) == 0:
                mp['zero'].append(s)
            elif len(s) == 1:
                mp['one'].append(s)
            else:
                key = tuple([(ord(s[i]) - ord(s[i - 1])) % 26 for i in range(1, len(s))])
                mp[key].append(s)
        return mp.values()
