class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicS = {}
        dicT = {}

        for i in s:
            if i in dicS:
                dicS[i] += 1
            else: dicS[i] = 1
        
        for i in t:
            if i in dicT:
                dicT[i] += 1
            else: dicT[i] = 1

        print(dicT)
        print(dicS)
        if dicS == dicT: return True
        return False
    
a = Solution()
print(a.isAnagram("rat", "car"))