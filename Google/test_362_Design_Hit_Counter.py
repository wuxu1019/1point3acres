"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);
Follow up:
What if the number of hits per second could be very large? Does your design scale?


"""


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [(0, 0)] * 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        p = timestamp % 300
        if self.data[p][1] != timestamp:
            self.data[p] = [1, timestamp]
        else:
            self.data[p][0] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        calc = 0
        for i in range(300):
            if timestamp - self.data[i][1] < 300:
                calc += self.data[i][0]
        return calc


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.deque()
        self.sumhits = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if self.data and timestamp == self.data[-1][0]:
            self.data[-1][1] += 1
        else:
            self.data.append([timestamp, 1])
        self.sumhits += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """

        while self.data and timestamp - self.data[0][0] >= 300:
            self.sumhits -= self.data.popleft()[1]

        return self.sumhits


