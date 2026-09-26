class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        pairs = {"[" : "]", "{" : "}", "(" : ")"}
        n = int(len(s))

        for c in s:
            if c in pairs.keys():
                stack.append(c)

            elif(len(stack) == 0):
                    return False
            
            elif pairs[stack[-1]] != c:
                return False

            else:
                stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False
                
