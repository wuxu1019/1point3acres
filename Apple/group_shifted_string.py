import collections

def groupShiftString(l):
    
    mp = collections.defaultdict(list)
    for s in l:
        diff = countDiff(s)
        mp[diff].append(s)
    return list(mp.values())


def countDiff(s):

    rt = "#"
    for i in range(len(s)-1):
        d = ord(s[i+1]) - ord(s[i])
        if d < 0:
            d += 26
        rt = rt + str(d) + "#"
    return rt


if __name__ == '__main__':
    l = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]
    rt = groupShiftString(l)
    print(rt)
