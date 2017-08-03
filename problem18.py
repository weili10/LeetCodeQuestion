'''
18. 4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such 
that a + b + c + d = target? Find all unique quadruplets in the array which 
gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        results = []
        self.findSum(nums, 4, target, result, results)
        return results

    def findSum(self, nums, N, target, result, results):
        if len(nums)<N or N<2:
            return

        if N == 2:
            l = 0
            r = len(nums)-1
            while l<r:
                if nums[r]+nums[l] == target:
                    results.append(result+[nums[r],nums[l]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[r]+nums[l] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):
                if target < nums[i]*N  or target > nums[-1]*N:
                    break
                if i == 0 or i>0 and nums[i-1] != nums[i]:
                    self.findSum(nums[i+1:], N-1, target - nums[i], result+[nums[i]], results)
        return





