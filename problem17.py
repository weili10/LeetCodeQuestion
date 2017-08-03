'''
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        dic = {'1':[],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'], '5':['j','k','l'],
        '6':['m','n','o'],'7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}

        result = []
        digits = str(digits)
        if len(digits) > 0:
            for i in range(len(dic[digits[0]])):
                result.append(dic[digits[0]][i])
        else:
            return result

        if len(digits) > 1:
            for i in range(1,len(digits)):
                newResult = []
                letters = dic[digits[i]]
                for j in range(len(result)):
                    for k in range(len(letters)):
                        newResult.append(result[j]+letters[k])
                result = newResult
        return result
        		

