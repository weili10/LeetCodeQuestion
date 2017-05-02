'''
12. Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Subscribe to see which companies asked this question.
'''
class Solution(object):
	def intToRoman(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		rom= [['M',1000], ['CM',900], ['D',500], ['CD',400], ['C',100], ['XC',90], ['L',50], ['XL',40], ['X',10], ['IX',9], ['V',5], ['IV',4], ['I',1]]
		roman = ""
		for i in range(len(rom)):
			while num - rom[i][1] >= 0:
				roman += rom[i][0]
				num -= rom[i][1]
		return roman
