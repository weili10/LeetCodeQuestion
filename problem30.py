'''
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
'''

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        n = len(words)
        l = len(s)
        if n == 0 or l == 0:
            return res
            
        k = len(words[0])
        
        bow = {}

        for word in words:
            bow[word] = bow.get(word,0)+1

        for i in range(l-k*n+1):
            nbow = {}
            count = 0
            for j in range(i,i+n*k,k):
                word = s[j:j+k]
                nbow[word] = nbow.get(word,0)+1
                if word not in bow or bow.get(word) < nbow.get(word):
                    break
                else:
                    count += 1
            if count == n:
                res.append(i)
            
        return res



