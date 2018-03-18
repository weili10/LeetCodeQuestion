'''
15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		result = []
		nums.sort();
		for i in range(len(nums)-2):
			if i == 0 or (i > 0 and nums[i] != nums[i-1]):
				j = i + 1
				k = len(nums)-1
				while j < k:
					if nums[i] + nums[j] + nums[k] == 0:
						result.append([nums[i],nums[j],nums[k]])
						while j < k and nums[k-1] == nums[k]:
							k -= 1
						while j < k and nums[j+1] == nums[j]:
							j += 1
						k -= 1
					elif nums[i] + nums[j] + nums[k] > 0:
						if nums[i] + nums[j] >= 0 and nums[j] > 0:
							break
						else:
							k -= 1
					else:
						if (nums[i] + nums[k] <= 0 and nums[k] < 0):
							break
						else:
							j += 1
		return result
