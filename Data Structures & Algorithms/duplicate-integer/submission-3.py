class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) == 0):
            return False

        uniqueNums = set()

        for n in nums:
            uniqueNums.add(n)
        
        if len(nums) != len(uniqueNums):
            return True
        else:
            return False
