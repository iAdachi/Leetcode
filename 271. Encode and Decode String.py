class Solution:
    def encode(self, strs: list[str]) -> str:
        output = ''
        for i in strs:
            output += str(len(i)) + '#' + i
        return output
    
    def decode(self, s: str) -> list[str]:
        output = []
        word = ''
        i = 0
        lenWord = 0

        while True:
            if i + 1 > len(s): break
            if s[i].isdigit() and s[i + 1] == "#": # finding Number#
                lenWord = int(s[i])
                i += 2
            else: i += 1
            
            while lenWord > 0:
                word += s[i]
                i += 1
                lenWord -= 1
            
            output.append(word)
            word = ''

        return output
