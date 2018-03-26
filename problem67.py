'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar = a[::-1]
        br = b[::-1]
        al = len(ar)
        bl = len(br)
        res = ''
        c = False 
        for i in range(min(al,bl)):
            res += '1' if (ar[i] == br[i] and c) or (ar[i] != br[i] and not c) else '0'
            if (ar[i] == br[i]) and ((ar[i] == '0' and c) or (ar[i] == '1' and not c)):
                c = not c 
                    
        z = ar[bl:al] if al > bl else br[al:bl]
            
        for i in range(len(z)):
            res += '1' if (z[i] == '1' and not c) or (z[i] == '0' and c) else '0'   
            c = True if z[i] == '1' and c else False
                   
        if c:
            res += '1' 
        return res[::-1]




