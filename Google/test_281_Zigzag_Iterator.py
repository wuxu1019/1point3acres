"""
Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6]

Output: [1,3,2,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,3,2,4,5,6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].

"""


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.data = collections.deque()
        for v in [v1, v2]:
            if v:
                self.data.append(collections.deque(v))

    def next(self):
        """
        :rtype: int
        """
        l = self.data.popleft()
        rt = l.popleft()
        if l:
            self.data.append(l)
        return rt

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.data:
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """

        self.data = [(len(v), iter(v)) for v in [v1, v2] if v]

    def next(self):
        """
        :rtype: int
        """
        lth, i = self.data.pop(0)
        rt = i.next()
        lth -= 1
        if lth:
            self.data.append((lth, i))
        return rt

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.data)

