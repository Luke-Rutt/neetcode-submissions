class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)
        h = n // 2
        
        for i in range(h):
            s[i], s[n-1-i] = s[n-1-i], s[i]
        