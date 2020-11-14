"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume 
that your function returns 0 when the reversed integer overflows.
 
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0

Constraints:

-2^31 <= x <= 2^31 - 1
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            reverse =  int(str(x * -1) [::-1]) * -1   
        else:
            reverse = int(str(x) [::-1])
    
        if int(reverse) >= 2**31-1 or int(reverse) <= -2**31: return 0
        return reverse