"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

"""


class Solution(object):
    def nextClosestTime_1(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = []
        for c in time:
            if c.isdigit():
                digits.append(int(c))
        digits.sort()

        hour_s, mini_s = time.split(':')
        hour = int(hour_s)
        mini = int(mini_s)

        for i in range(len(digits)):
            for j in range(len(digits)):
                m = digits[i] * 10 + digits[j]
                if 0 <= m < 60:
                    if m > mini:
                        if m >= 10:
                            return '{0}:{1}'.format(hour_s, m)
                        else:
                            return '{0}:0{1}'.format(hour_s, m)
                else:
                    break
        for i in range(len(digits)):
            for j in range(len(digits)):
                m = digits[i] * 10 + digits[j]
                if 0 <= m < 24:
                    if m > hour:
                        if m >= 10:
                            return '{0}:{1}{1}'.format(m, digits[0])
                        else:
                            return '0{0}:{1}{1}'.format(m, digits[0])
                else:
                    break

        return '{0}{0}:{0}{0}'.format(digits[0])

    def nextClosestTime_2(self, time):
        """
        :type time: str
        :rtype: str
        """
        p = time.index(':')
        h, m = int(time[:p]), int(time[p + 1:])
        base = h * 60 + m
        cycle = 24 * 60
        mindiff = cycle
        ans = int(time[:p]) * 60 + int(time[p + 1:])
        allowed = set([int(i) for i in time if i.isdigit()])

        for ha, hb, ma, mb in itertools.product(allowed, repeat=4):
            h = ha * 10 + hb
            m = ma * 10 + mb
            if 0 <= h < 24 and 0 <= m < 60:
                cur = h * 60 + m
                diff = (cur - base) % cycle

                if diff > 0 and diff < mindiff:
                    mindiff = diff
                    ans = cur

        return '{0:02d}:{1:02d}'.format(*divmod(ans, 60))


    def nextClosestTime_3(self, time):

        return min((t <= time, t)
                   for i in range(24 * 60)
                   for t in ['%02d:%02d' % divmod(i, 60)]
                   if set(t) <= set(time))[1]
