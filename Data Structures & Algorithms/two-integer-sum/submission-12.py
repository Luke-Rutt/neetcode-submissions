class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        J = {}

        for j in range(len(nums)):
            J[j] = nums[j:len(nums)]

        for i in range(len(nums)-1):
            j = i+1
            difference = target - nums[i]
            if difference in J[j]:
                k = J[j].index(difference) + j
                return [i, k]
