'''
69. Sqrt(x)

mplement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
'''

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        else:
            return self.mySqrt1(x,0,x)

    def mySqrt1(self,x,low,high):
        mid = int((low+high)/2)
        if mid*mid <= x:
            if (mid+1)*(mid+1)>x:
                return mid
            else:
                return self.mySqrt1(x,mid,high)
        else:
            return self.mySqrt1(x,low,mid)


