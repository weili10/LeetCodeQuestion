'''
10. Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
isMatch("", "c*") → true
isMatch("", ".") → false
isMatch("", ".*") → true

'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        sl = list(s)
        pl = list(p)

        dp = [([False]*(len(pl)+1)) for i in range(len(sl)+1)]
        dp[0][0] = True;

        for i in range(len(pl)):
        	if pl[i] == "*" and dp[0][i-1]:
        		dp[0][i+1] = True;

        for i in range(len(sl)):
        	for j in range(len(pl)):
        		if pl[j] == ".":
        			dp[i+1][j+1] = dp[i][j]
        		if pl[j] == sl[i]:
        			dp[i+1][j+1] = dp[i][j]
        		if pl[j] == "*":
        			if pl[j-1] != sl[i] and pl[j-1] != ".":
        				dp[i+1][j+1] = dp[i+1][j-1]
        			else:
        				dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]

        return dp[len(sl)][len(pl)]



