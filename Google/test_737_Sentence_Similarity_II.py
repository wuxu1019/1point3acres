"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""


class DSU(object):
    def __init__(self, N):
        self.par = range(N)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)


class Solution(object):
    def areSentencesSimilarTwo_unionfind(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        uf = DSU(2 * 1001)
        i = 0
        mp = {}
        for pair in pairs:
            for word in pair:
                if word not in mp:
                    mp[word] = i
                    i += 1
            uf.union(mp[pair[0]], mp[pair[1]])

        return all(words1[i] == words2[i] or words1[i] in mp and words2[i] in mp and uf.find(mp[words1[i]]) == uf.find(
            mp[words2[i]]) for i in range(len(words1)))

    def areSentencesSimilarTwo_dfs(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        mp = collections.defaultdict(set)
        for a, b in pairs:
            mp[a].add(b)
            mp[b].add(a)

        self.similar = {}

        def dfs(node, root):
            if node in self.similar:
                return
            self.similar[node] = root
            for v in mp[node]:
                dfs(v, root)

        for k in mp.keys():
            dfs(k, k)

        return all(
            self.similar.get(word1, word1) == self.similar.get(word2, word2) for word1, word2 in zip(words1, words2))

