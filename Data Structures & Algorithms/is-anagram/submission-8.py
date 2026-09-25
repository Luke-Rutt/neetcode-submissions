class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False
        
        dict1 = {}
        dict2 = {}

        q = len(s)

        for n, i in enumerate(s):
            dict1[n] = s[n]
            dict2[n] = t[n]
        
        if sorted(dict1.values()) == sorted(dict2.values()):
            return True
        else:
            return False