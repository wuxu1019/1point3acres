
def revertArray(array, N):

    rt = []

    for i in range(0, len(array), N):
        rt.extend(array[i:i+N][::-1])
    return rt

if __name__ == '__main__':
    array = range(1, 10)
    N = 3
    rt = revertArray(array, N)
    print rt