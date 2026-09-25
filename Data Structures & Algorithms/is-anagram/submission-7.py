class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        dictS = {}
        dictT = {}

        for i in range(0, len(s)):
            dictS[s[i]] = dictS.get(s[i], 0) + 1
            dictT[t[i]] = dictT.get(t[i], 0) + 1

        if dictS == dictT:
            return True
        else:
            return False 
            
