class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)
        
        for i, num in enumerate (nums):
            if num == val:
                nums[i] = "_"
            else:
                nums[k] = num
                k+=1
        
        return k
            

            
                