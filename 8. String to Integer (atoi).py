class Solution(object):
    def checks(self, r, n):
        """
        :type r: str
        :rtype: int
        """
        if r == '': return 0
        r = int(r)
        if n * r > 2 ** 31 - 1: return 2 ** 31 - 1
        if n * r < -1 * 2 ** 31: return -1 * (2 ** 31)
        return n * r

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        negative = 1
        if len(s) == 0: return 0
        if s[0] == '-': 
            negative = -1
            s = s[1:] 
        elif s[0] == '+': s = s[1:]
        result = ''
        for i in s:
            try:
                result += str(int(i))
            except:
                return self.checks(result, negative)
        return self.checks(result, negative)
