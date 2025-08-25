class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1: return False 
        
        keys = {"}":"{", ")":"(", "]":"["}
        stack = []
        
        for i in s:
            if i in keys.values(): # if is '(', '[' or '{'
                stack.append(i)
            elif stack and stack[-1] == keys[i]: # if stack is not empty 
                stack.pop()
            else: return False 
        
        if stack: return False # if stack is not empty
        return True
