"""
Description
Given some intervals, ask how many are covered most, if there are multiple, output the smallest number.

the number of the interval is not more than 10^5.
the left and right endpoints of the interval are greater than 0 not more than 10^5.
Have you met this question in a real interview?
Example
Given intervals = [(1,7),(2,8)], return 2.

Explanation:
2 is covered 2 times, and is the number of 2 times the smallest number.
Given intervals = [(1,3),(2,3),(3,4)], return 3.

Explanation:
3 is covered 3 times.
DifficultyMedium
Total Accepted317
Total Submitted1041
Accepted Rate30%
 Show Tags
 Company

"""

class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """
    def digitalCoverage(self, intervals):
        # Write your code here
        maxend = max(interval.end for interval in intervals)
        record = [0] * (maxend+2)
        for interval in intervals:
            record[interval.start] += 1
            record[interval.end+1] -= 1
        maxsum = 0
        maxloc = 0
        sum = 0
        for i in range(1, maxend+2):
            sum += record[i]
            if sum > maxsum:
                maxsum = sum
                maxloc = i
        return maxloc

if __name__ == '__main__':
    s = Solution()
    interval = [(1,3),(2,3),(3,4)]
    rt = s.digitalCoverage(intervals)
    print rt