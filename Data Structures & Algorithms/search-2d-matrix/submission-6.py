class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix)-1
        m1 = 0
        row = 0

        while t <=b:
            m1 = (t+b)//2
            if target < matrix[m1][0]:
                b = m1-1
            elif target > matrix[m1][-1]:
                t = m1 + 1

            else:
                row = m1
                break
        
        l = 0
        r = len(matrix[m1]) - 1

        while l<=r:
            m2 = (l+r)//2
            if(matrix[row][m2] == target):
                return True
            
            elif target < matrix[row][m2]:
                r = m2 - 1

            elif target > matrix[row][m2]:
                l = m2 + 1
            
        
        return False

            
        
