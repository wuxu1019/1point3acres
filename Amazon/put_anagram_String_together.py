"""
put anagram string together
"""
import collections

def findAnagramStringGroups(strings):

    groups = collections.defaultdict(list)
    for s in strings:
        key = [0] * 256
        ct = collections.Counter(s)
        for k, v in ct.items():
            key[ord(k)] += v
        groups[tuple(key)].append(s)

    return [v for v in groups.values()]

if __name__ == '__main__':
    strings = ['abc', 'bca', 'cba', 'bb', 'cc', 'bb']
    rt = findAnagramStringGroups(strings)
    print rt