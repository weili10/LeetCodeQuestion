class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        if length <1: return 0
        i = 0
        while i < length:
            if nums[i] == val:
                del nums[i]
                length -= 1
            else:
                i += 1

        return len(nums)