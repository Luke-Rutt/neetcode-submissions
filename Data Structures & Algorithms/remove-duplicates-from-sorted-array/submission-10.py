class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        k = r = 1
        n = len(nums)


        while (r < n):
            if(nums[l] == nums[r]):
                nums.pop(r)
                n = len(nums)
                
            else:
                k+=1
                l+=1
                r+=1

        return k

                
               
