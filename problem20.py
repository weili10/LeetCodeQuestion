'''
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(':1,')':-1,'[':2,']':-2,'{':3,'}':-3}
        stack = []
        for i in range(len(s)):
            if dic[s[i]] > 0 :
                stack.append(dic[s[i]])
            elif dic[s[i]] < 0 :
                if len(stack) == 0 or stack.pop()+dic[s[i]] != 0:
                return False
        if len(stack) > 0:
            return False
        else:
            return True
        