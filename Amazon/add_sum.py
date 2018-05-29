"""
find a^2 + b^2 + c ^ 2 + d^2 = k
all the combination
"""
import math
def find_combination1(k):
    p = int(math.sqrt(k))
    ans = set()
    for a in range(1, p):
        for b in range(1, p):
            for c in range(1, p):
                for d in range(1, p):
                    if a * a + b * b + c * c + d * d == k:
                        ans.add(tuple(sorted([a, b, c, d])))
    return [list(i) for i in ans]



if __name__ == '__main__':
    rt = find_combination1(100)
    print rt
