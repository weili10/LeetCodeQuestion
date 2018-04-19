'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        index = None
        for i in range(l-1,0,-1):
            if nums[i] > nums[i-1]:
                index = i
                break
        if index == None:
            nums.reverse()
            # return nums
        else:
            swaped = False
            for i in range(0,int((l-index)/2)):
                temp = nums[index+i]
                nums[index+i] = nums[l-1-i]
                nums[l-1-i] = temp
            for i in range(index,l):
                if nums[i] > nums[index-1]:
                    temp = nums[i]
                    nums[i] = nums[index-1]
                    nums[index-1] = temp
                    break
            # return nums


            
            

