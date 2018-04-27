
import itertools
import collections
def count_max_o_round_x(l):
    ct = [len(list(g)) for p, g in itertools.groupby(l) if p == 'O']
    return max([i + j for i, j in zip(ct + [0], [0] + ct)])

def count_max_o_round_x_2(l):
    before, after = 0, 0
    p1 = l.index('X')


def removeSpace(l):
    if len(l) == 0:
        return l
    if len(l) == 1:
        return None if l == [' '] else l

    i = -1
    for j in range(0, len(l)):
        if l[j] != ' ':
            i += 1
            l[i] = l[j]
    return l[:i + 1]

def revertIngeter(num):

    rt = 0
    while num:
        num, res = divmod(num, 10)
        rt = rt * 10 + res
    return rt

def canConstruct(s1, s2):
    ct1 = collections.Counter(s1)
    ct2 = collections.Counter(s2)


    return not ct1 - ct2


if __name__ == '__main__':
    l = 'OOOXOOOOXOXOOOOXOXXOOOO'
    rt = count_max_o_round_x(l)
    print rt

    st = '  AA BB BBA'
    l = list(st)
    rt = removeSpace(l)
    print ''.join(rt)

    num = 146
    print revertIngeter(num)

    print canConstruct('aabbb', 'aaabb')



