
import collections
def sort_array(l):
    ct = collections.Counter(l)
    ct.most_common()

    rt = ''
    for k, v in ct.items():
        rt += k * v
    return rt

if __name__ == '__main__':
    l = 'ABABASDAWQRQWMSDASDABABASDA'
    rt = sort_array(l)
    print rt