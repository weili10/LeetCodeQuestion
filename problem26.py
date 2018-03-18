class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1 : return nums
        length = len(nums)
        i = 1
        while i<length:
            if nums[i] == nums[i-1]:
                del nums[i-1]
                length = length -1
            else:
                i = i+1
        return nums
            