"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
"""


class Solution(object):
    def findMaxConsecutiveOnes_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rt = 0
        ct = []
        for a, b in itertools.groupby(nums):
            ct.append((a, len(list(b))))

        for i, v in enumerate(ct):
            a, n = v[0], v[1]
            if a == 0:
                if n == 1:
                    summ = 0
                    summ += ct[i - 1][1] if i - 1 >= 0 else 0
                    summ += n
                    summ += ct[i + 1][1] if i + 1 < len(ct) else 0
                    rt = max(rt, summ)
                else:
                    before = ct[i - 1][1] + 1 if i - 1 >= 0 else 1
                    after = ct[i + 1][1] + 1 if i + 1 < len(ct) else 1
                    rt = max(before, after, rt)
            else:
                rt = max(rt, n)
        return rt

    def findMaxConsecutiveOnes_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pre, cur, maxlth = -1, 0, 0

        for num in nums:
            if num == 0:
                pre, cur = cur, 0
            else:
                cur += 1
            maxlth = max(maxlth, pre + cur + 1)
        return maxlth

    def findMaxConsecutiveOnes_slidewindow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        zeros = 0
        maxlth = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            maxlth = max(maxlth, r - l + 1)
        return maxlth
