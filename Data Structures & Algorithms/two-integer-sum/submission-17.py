class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers = {}

        for i, x in enumerate (nums):
            diff = target - nums[i]


            if diff in numbers:
                return [numbers[diff], i]
            
            numbers[x] = i

            

