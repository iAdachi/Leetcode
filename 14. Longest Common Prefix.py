class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs = list(set(strs))
        result = ''
        letterPosition = 0
        while True:
            for i in range(len(strs)):
                try:
                    if strs[0][letterPosition] != strs[i][letterPosition]:
                        return result
                except:
                    return result
            result += strs[0][letterPosition]
            letterPosition += 1


