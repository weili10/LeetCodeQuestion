'''
66. Plus One

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1:
            if digits[0] == 9:
                return [1,0]
            else:
                return [digits[0]+1]

        if digits[-1] == 9:
            digits = self.plusOne(digits[:-1])+[0]
            # can not use .append() here because .append() doesn't return the new list
        else:
            digits[-1] += 1
        return digits