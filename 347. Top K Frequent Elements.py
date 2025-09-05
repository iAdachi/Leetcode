class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in nums:
            if i in hashMap: hashMap[i] += 1
            else: hashMap[i] = 1
        
        maxFreq = -10 ** 4 - 1
        for i in hashMap.values(): # looking for maximun frequency
            if i > maxFreq: maxFreq = i
        
        hashFreq = {} # frequencie : [value1, value2...]
        for i in range(maxFreq): # initialize hashFreq
            hashFreq[i+1] = []
        
        for key, value in hashMap.items():
            hashFreq[value].append(key)

        result = []
        for key, value in reversed(list(hashFreq.items())): # from maximun frequency to minimum
            for v in value:
                if len(result) < k: result.append(v)
                else: break
        
        return sorted(result)

    def topKFrequent1(self, nums, k): # my attempt
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashMap = {}
        for i in nums:
            if i in hashMap: hashMap[i] += 1
            else: hashMap[i] = 1

        setNums = list(set(nums))
        biggestFreq = - 10**4 - 1
        indexB = -1 
        result = []
        
        while k > 0 and len(result) < len(setNums):
            for i in setNums:
                if hashMap[i] > biggestFreq and i not in result:
                    indexB = i 
                    biggestFreq = hashMap[i] 

            result.append(indexB)
            biggestFreq = - 10**4 - 1
            k -= 1

        return sorted(result)