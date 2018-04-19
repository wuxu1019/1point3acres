

def changestring(s):
    l = s.split(',')
    rt = []
    for a in l:
        a = a.lstrip(' ')
        a = a.rstrip(' ')
        if a:
            rt.append(int(a))
    return rt


if __name__ == '__main__':
    target = "1,,,,  3434, 22, , 345, 6, ,4,"
    result = changestring(target)
    print result