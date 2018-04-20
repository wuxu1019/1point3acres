"""
Given the following set of strings, write a function that stores this information.

// /Electronics/Computers/Graphics Cards
// /Electronics/Computers/Graphics Cards
// /Electronics/Computers/SSDs
// /Electronics/Computers/Graphics Cards
// /Electronics/Computers/SSDs
// /Electronics/TVs
// /Electronics/Computers/Graphics Cards
// /Electronics/TVs
// /Electronics/TVs
// /Garden
// /Automotive/Parts

Your datastructure should be able to provide information as such:
// / = 11
// /Electronics = 9
// /Electronics/Computers = 6
// /Electronics/Computers/Graphics Cards = 4
// /Electronics/TVs = 3
// etc
// ["/Electronics/Computers/Graphics Cards", "/Garden"]
"""


class TreeNode(object):
    def __init__(self, val, end):
        self.val = val
        self.end = end
        self.next = {}


class Record(object):
    def __init__(self):
        self.root = TreeNode(0, False)

    def insertLines(self, lines):
        for line in lines:
            self.insertLine(line)

    def insertLine(self, line):
        self.root.val += 1
        if line == '/':
            self.root.end = True
            return
        line = line.split('/')[1:]
        p = self.root

        for i, chars in enumerate(line):
            if chars in p.next:
                p.next[chars].val += 1
            else:
                p.next[chars] = TreeNode(1, False)
            if i == len(line) - 1:
                p.next[chars].end = True
            p = p.next[chars]

    def findChildAmount(self, target):
        if target == '/':
            return self.root.val
        li = target.split('/')[1:]
        return self.findChildAmountHelper(self.root, 0, li)

    def findChildAmountHelper(self, root, p, l):
        if p >= len(l) or l[p] not in root.next:
            return 0
        if p == len(l) - 1:
            return root.next[l[p]].val
        return self.findChildAmountHelper(root.next[l[p]], p+1, l)

    def outputFileNames(self):
        if self.root.end:
            files = ['/']
        else:
            files = []
        self.travesal(self.root, "", files)
        return files

    def travesal(self, root, base, l):
        if root.end and base:
            l.append(base)
        for k, v in root.next.items():
            self.travesal(v, base + '/' + k, l)


if __name__ == '__main__':
    r = Record()
    lines = [
        "/Electronics/Computers/Graphics Cards",
        "/Electronics/Computers/SSDs",
        "/Electronics/Computers/Graphics Cards",
        "/Electronics/TVs",
        "/Electronics/TVs",
        "/Electronics/TVs",
        "/Electronics/TVs",
        "/Electronics/Computers/Graphics Cards",
        "/Electronics/Computers/SSDs",
        "/Electronics/Computers/Graphics Cards",
        "/Electronics/TVs",
        "/Electronics/TVs",
        "/Electronics/TVs",
        "/Electronics/TVs",
        "/Garden",
        "/Automotive/Parts",
        "/"

    ]
    r.insertLines(lines)
    rt1 = r.findChildAmount('/Electronics/Computers/Graphics Cards')
    print rt1

    rt2 = r.outputFileNames()
    print rt2



