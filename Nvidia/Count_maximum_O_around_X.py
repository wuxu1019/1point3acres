
import itertools
def count_max_o_round_x(l):
    ct = [len(list(g)) for p, g in itertools.groupby(l) if p == 'O']
    return max([i + j for i, j in zip(ct + [0], [0] + ct)])

if __name__ == '__main__':
    l = 'OOOXOOOOXOXOOOOXOXXOOOO'
    rt = count_max_o_round_x(l)
    print rt