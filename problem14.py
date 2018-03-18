'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

'''

class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if len(strs) == 0:
		    return ""
		strs.sort()
		prefix = ""
		a = strs[0]
		b = strs[len(strs)-1]
		for i in range(len(strs[0]):
			if b[i] == a[i]:
				prefix += a[i]
			else:
				return prefix
		return prefix