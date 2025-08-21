class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        
        listS = []
        for i in range(numRows):
            listS.append([])
        
        upDown = 1
        positionRow = 0
        
        for i in s:
            listS[positionRow].append(i)
            
            if positionRow == 0:
                upDown = 1

            elif positionRow >= numRows - 1:
                upDown = -1
            positionRow += upDown
        
        result = '' 
        for subS in listS:
            result += ''.join(subS)
        return result
    
    def convert_1(self, s, numRows):
        if numRows == 1: return s
        
        listS = []
        for i in range(numRows):
            listS.append([])
        
        upDown = False # False -> down, true -> up
        positionRow = 0
        for i in s:
            listS[positionRow].append(i)
            
            if upDown == False: positionRow += 1
            else: positionRow -= 1
                
            if positionRow > numRows-1:
                upDown = True
                positionRow -= 2
            elif positionRow < 0:
                upDown = False
                positionRow += 2

        textS = '' 
        for subS in listS:
            textS += ''.join(subS)
        
        return textS
    
    def convert_2(self, s, numRows):
        if numRows == 1:
            return s
        
        x = y = 0
        letterPosition = 0
        saveXY = {}
        
        while letterPosition < len(s):
            if x not in saveXY:
                saveXY[x] = {}
            
            saveXY[x][y] = s[letterPosition]
            letterPosition += 1
            if y >= numRows -1:
                while y != 0 and letterPosition < len(s):
                    x += 1
                    y -= 1
                    if x not in saveXY:
                        saveXY[x] = {}
                    saveXY[x][y] = s[letterPosition]
                    letterPosition += 1
            y += 1

        newS = ''
        for i in range(numRows):
            for sub in saveXY.values():
                if i in sub:
                    newS += sub[i]
        
        return newS

