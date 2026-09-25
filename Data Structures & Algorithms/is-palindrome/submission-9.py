class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        t = list(s.strip().upper().replace(" ", ''))

        u = []

        for c in t:
            if c.isalnum():
                u.append(c)

        for i in range(0, len(u)):
            if u[i] != u[len(u)-1 - i]:
                return False
        
        return True