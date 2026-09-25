class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]

        n = len(cleaned)
        h = n // 2

        for i in range(h):
            if(cleaned[i] != cleaned[n-1-i]):
                return False
        
        return True