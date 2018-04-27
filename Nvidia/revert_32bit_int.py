# revert 32 bit int by 8 bit

def revert32bit(num):
    i = 2**9 - 1
    rt = 0
    for j in range(4):
        p = 8 * j
        rt |= (num ^ i) << p
        num = num >> 8
    return rt

if __name__ == '__main__':
    num = 435
    print bin(num)
    rt = revert32bit(num)
    print rt
    print bin(rt)