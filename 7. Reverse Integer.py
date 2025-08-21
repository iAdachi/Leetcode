class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = 1
        if x < 0: 
            f = -1 
            x = x * -1

        result = 0
        numMax = (2 ** 31) // 10
        
        while True:
            m = x % 10
            x = x // 10
            
            if result > numMax or f * result < -1 * numMax: return 0
            
            result = result * 10 + m 
            if x == 0: return f * result
            
    def reverse_1(self, x):
        if x < -2**31 or x > 2**31 -1: return 0

        d = 1
        if x < 0:
            d = -1
            x *= -1
        
        xStr = str(x)
        result = d*int(xStr[::-1])
        if result < -2**31 or result > 2**31 -1: return 0
        return result