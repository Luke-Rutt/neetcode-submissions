class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pair = [0, 0]
        numbers = {}

        for i, x in enumerate (nums):
            diff = target - nums[i]


            if diff in numbers:
                return [numbers[diff], i]
            
            numbers[x] = i

            

