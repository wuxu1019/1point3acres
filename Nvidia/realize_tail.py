"""
Implement the unix Tail utility. (given a stream of lines from a file or program print only the last N lines of said stream.)
.1
"""

def tail(filename, k):
    rt = []
    with open(filename, 'r') as fp1:
        with open(filename, 'r') as fp2:
            for line1 in fp1:
                k -= 1
                if k == 0:
                    break
            for line1 in fp1:
                line2 = fp2.readline()
            for line2 in fp2:
                rt.append(line2)
                print line2
    return rt

if __name__ == '__main__':
    rt1 = tail('threading.py', 4)

