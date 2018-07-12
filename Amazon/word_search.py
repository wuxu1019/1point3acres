"""
give a string and an dictionary. Ask for breaking the string by the words given in the dictionary
"""

class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.next = {}

def splitStringByWords(s, words):
    root = TrieNode(False)
    for word in words:
        putToTree(root, word)

    i = 0
    sub = ''
    rt = []
    while i < len(s):
        j = findWord(root, s, i)
        if j < 0:
            sub += s[i]
            i += 1
        else:
            i += j
            rt.append(sub)
            sub = ''
    rt.append(sub)

    return rt


def findWord(root, s, i):
    p = root
    j = 0
    while i < len(s):
        if p.val == True:
            return j
        if s[i] not in p.next:
            return -1
        p = p.next[s[i]]
        i += 1
        j += 1
    if p.val == True:
        return j
    return -1


def putToTree(root, word):

    p = root
    for c in word:
        if c not in p.next:
            p.next[c] = TrieNode(False)
        p = p.next[c]

    p.val = True


if __name__ == '__main__':
    s = 'bigdogbig'
    words = ['big', 'dog']
    rt = splitStringByWords(s, words)
    print rt