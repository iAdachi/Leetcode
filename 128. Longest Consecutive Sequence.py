class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        setNums = set(nums)
        nums = list(setNums)
        longest = 0

        for i in nums:
            if i - 1 in setNums: continue

            lenght = 0
            while i + lenght in setNums: # finding sequence 
                lenght += 1
            longest = max(lenght, longest)

        return longest

    def longestConsecutive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        setNums = set(nums)
        nums = list(setNums)
        sequence = []

        for i in nums:
            if i - 1 in setNums: continue # is not the begin of the sequence

            subsequence = []
            j = i
            while j in setNums: # finding sequence 
                subsequence.append(j)
                j += 1
            sequence.append(subsequence)

        longestSequence = 0
        for i in sequence:
            if len(i) > longestSequence: longestSequence = len(i)

        return longestSequence


