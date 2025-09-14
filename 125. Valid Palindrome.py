class Solution(object):
    def normalization(self, string):
        string = string.replace(" ", "")
        string = string.lower()
        alphanumeric = set('abcdefghijklmnopqrstuvwxyz1234567890')
        output = ''
        for i in string:
            if i in alphanumeric:
                output += i

        return output
    
    def isPalindrome(self, s):
        s = self.normalization(s)
        i = 0
        j = len(s) - 1

        while i < j:
            print(s[i], s[j])
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        
        return True

    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = self.normalization(s)
        if s == s[::-1]: return True
        return False