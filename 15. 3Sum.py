class Solution(object):
    def partition(self, l, h , unorderedL):
        pivot = unorderedL[l]
        i = l #+ 1
        j = h - 1

        while i < j:
            while unorderedL[i]<= pivot and i + 1 < len(unorderedL):
                i += 1
            
            while unorderedL[j] > pivot and j - 1 >= 0:
                j -= 1

            if i < j:
                unorderedL[i], unorderedL[j] = unorderedL[j], unorderedL[i]

        unorderedL[l], unorderedL[j] = unorderedL[j], unorderedL[l]
        return j

    def quickSort(self, l, h , unorderedL):
        if l < h:
            j = self.partition(l, h , unorderedL)
            self.quickSort(l, j , unorderedL)
            self.quickSort(j + 1, h , unorderedL)
        return unorderedL

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        sortedNums = self.quickSort(0, len(nums), nums)
        output = []
        
        i = 0
        while i < len(sortedNums) - 1:
            j = i + 1
            k = len(sortedNums) - 1

            while j < k: # j contain negative numbers and k, positive
                if sortedNums[i] + sortedNums[j] + sortedNums[k] == 0:
                    output.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    
                    tempJ = sortedNums[j]
                    tempK = sortedNums[k]
                    while tempJ == sortedNums[j] and j + 1 < k: j += 1 # change the number
                    while tempK == sortedNums[k] and k - 1 > 0: k -= 1 

                if sortedNums[i] + sortedNums[j] + sortedNums[k] > 0: k -= 1 # infinite -> 0
                if sortedNums[i] + sortedNums[j] + sortedNums[k] < 0: j += 1 # -infinite -> 0
            
            tempI = sortedNums[i]
            while tempI == sortedNums[i] and i + 1 < len(sortedNums): i += 1
        return output

