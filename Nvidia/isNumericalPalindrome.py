"""
Determine if a number is a numerical palindrome:

Yes: 1, 9, 121 , 3003
Numbers that aren’t are: 10 100 402.

bool isNumericalPalindrome(unit32 number, uint32 base (Like base 10,  base 16 base 7);

"""

def isNumericalPalindrome(num, base):
    p1, p2, mul = 0, 0, 1

    while num > 0:
        num, rem = divmod(num, base)
        p1 += mul * rem
        p2 = p2 * 10 + rem
        mul *= 10
    return p1 == p2

if __name__ == '__main__':
    nums = 235
    base = 11
    rt1 = isNumericalPalindrome(nums, base)
    print rt1
    nums = 12321
    base = 10
    rt2 = isNumericalPalindrome(nums, base)
    print rt2