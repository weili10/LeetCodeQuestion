'''
34. Search for a Range

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        
        low, high = 0, len(nums)-1
        start ,end = -1,-1

        while low <= high:
            mid = int((low+high)/2)
            if target == nums[mid]:
                if (mid -1 >= 0 and target > nums[mid-1]) or mid == 0:
                    start = mid
                    break
                else:
                    high = mid - 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        if start == -1:
            return [-1,-1]
        else:
            low,high = start, len(nums)-1

            while low <= high:
                mid = int((low+high)/2)

                if target == nums[mid]:
                    if (mid+1 <= len(nums)-1 and target < nums[mid+1]) or mid == len(nums)-1:
                        end = mid
                        return [start,end]
                    else:
                        low = mid + 1
                else:
                    high = mid - 1











