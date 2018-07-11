import collections

def stringPermutation_1(s):

    # if here is no repeat character in string

    rt = []

    def permutationHelper(st, base, lth):

        if len(base) == lth:
            rt.append(base)
            return
        for i in range(len(st)):
            permutationHelper(st[:i] + st[i+1:], base + st[i], lth)

    permutationHelper(s, '', len(s))
    return rt

def stringPermutation_2(s):

    # if here is repeat character in string

    rt = []

    def permutationHelper(ct, base, lth):
        if len(base) == lth:
            rt.append(base)
            return

        for k, v in ct.items():
            if v > 0:
                ct[k] = v - 1
                permutationHelper(ct, base + k, lth)
                ct[k] = v
    ct = collections.Counter(s)
    permutationHelper(ct, '', len(s))
    return rt

if __name__ == '__main__':

    s1 = 'ABCD'
    rt1 = stringPermutation_1(s1)
    print rt1
    print len(rt1)

    s2 = 'AAAAAB'
    rt2 = stringPermutation_2(s2)
    print rt2
    print len(rt2)

