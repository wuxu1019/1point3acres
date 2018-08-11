"""
Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]

"""

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        calc = [ a * num * num + b * num + c for num in nums ]
        i, j = 0, len(nums)-1
        rt = []
        while i <= j:
            if a > 0:
                if calc[i] > calc[j]:
                    rt.append(calc[i])
                    i += 1
                else:
                    rt.append(calc[j])
                    j -= 1
            else:
                if calc[i] < calc[j]:
                    rt.append(calc[i])
                    i += 1
                else:
                    rt.append(calc[j])
                    j -= 1
        if a > 0:
            return rt[::-1]
        else:
            return rt