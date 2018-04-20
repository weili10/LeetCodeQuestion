'''
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*len(s)   # dp[i]  the longest valid parenthesess that end with s[i]
        maxlen = 0
        for i in range(1,len(s)):
            if s[i] == "(":
                dp[i] = 0
            if s[i] == ")":
                if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-1]+2
                    if i - dp[i-1] -2 >0:
                        dp[i] += dp[i - dp[i-1] -2]
            maxlen = max(maxlen,dp[i])
        return maxlen


