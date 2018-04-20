"""
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""

def singleNonDuplicate(nums):
    lo, hi = 0, len(nums)-1
    while lo < hi:
        mid = lo + (hi - lo) / 2
        if nums[mid] == nums[mid ^ 1]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3, 4, 4, 5, 5]
    rt1 = singleNonDuplicate(nums)
    print rt1