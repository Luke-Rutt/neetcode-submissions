class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dup = {}

        for i, num in enumerate(nums):
            dup[num] = dup.get(num,0) + 1
        
        majority = max(dup, key=dup.get)

        return majority
