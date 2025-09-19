class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
    
    def findMinV1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1: return 0
        if nums[0] < nums[-1]: return nums[0]
        prev = nums[0]
        for i in nums:
            if i < prev: return i
            prev = i
        return nums[0]
    
    def findMinV2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 1: return 0 

        while nums[0] > nums[-1]:
            nums.insert(0, nums[-1])
            nums.pop()
        return nums[0]


        