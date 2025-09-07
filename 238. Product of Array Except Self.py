class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = [1]
        l = [1]
        
        mul = 1
        for i in nums:
            if len(r) < len(nums):
                mul *= i
                r.append(mul)

        mul = 1
        nums.reverse()
        for i in nums:
            if len(l) < len(nums):
                mul *= i
                l.append(mul) 
        l.reverse()
        
        result = []
        for i, j in zip(r, l):
            result.append(i * j)
        return result
