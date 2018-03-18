'''
89. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
'''

'''
main idea 
given     00 01 11 10
       1  00 extend to 000 001
       2  01 extend to 010 011
       3  11 extend to 110 111
       4  10 extend to 100 101
to make new codes become gray code
just switch the position extended from EVEN rows
like      00 01 11 10
       1  00 extend to 000 001
       2  01 extend to 011 010 
       3  11 extend to 110 111
       4  10 extend to 101 100

'''
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        
        sgc = self.grayCode(n-1)
        res = []
        odd = True
        for code in sgc:
            if odd:
                res.extend([code*2,code*2+1])
                odd = False
            else:
                res.extend([code*2+1,code*2])
                odd = True
        return res