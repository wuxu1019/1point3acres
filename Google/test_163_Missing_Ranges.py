"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

"""


class Solution(object):
    def findMissingRanges_1(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        if not nums:
            if lower == upper:
                return [str(upper)]
            else:
                return [str(lower) + '->' + str(upper)]

        rt = []
        if lower != nums[0]:
            nums = [lower - 1] + nums
            last = lower - 1
        else:
            last = lower

        if upper != nums[-1]:
            nums = nums + [upper + 1]

        for i in range(len(nums)):
            if nums[i] != last:
                if nums[i] != last + 1:
                    left, right = last + 1, nums[i] - 1
                    if left == right:
                        rt.append(str(left))
                    else:
                        rt.append(str(left) + '->' + str(right))
            last = nums[i]
        return rt

    def findMissingRanges_short(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        nums.append(upper + 1)
        last = lower - 1
        rt = []
        for num in nums:
            if num == last + 2:
                rt.append(str(num - 1))
            elif num > last + 2:
                rt.append(str(last + 1) + '->' + str(num - 1))
            last = num
        return rt