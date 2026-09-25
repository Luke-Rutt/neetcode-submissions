class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0

        word3 = []

        while(l < len(word1) or r < len(word2)):
            if len(word1) > l:
                word3.append(word1[l])
                l+=1
            if len(word2) > r:
                word3.append(word2[r])
                r+=1

        return ''.join(word3)
