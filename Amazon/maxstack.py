
class MaxStack(object):

    def __init__(self):
        self.stk = []


    def push(self, val):
        if not self.stk:
            self.stk.append((val, val))

        else:
            self.stk.append((val, max(self.stk[-1][1], val)))

    def pop(self):
        if not self.stk:
            return None
        return self.stk.pop()[0]

    def maxval(self):
        if not self.stk:
            return None
        return self.stk[-1][1]

if __name__ == '__main__':
    s = MaxStack()
    print s.maxval()
    print s.pop()

    s.push(1)
    print s.maxval()
    print s.pop()

    s.push(1)
    s.push(3)
    print s.maxval()
    print s.pop()
    print s.maxval()