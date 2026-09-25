class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = 0
        r = 0
        nums3 = []

        while (l < m or r < n):
                if (l == m):
                    nums3.append(nums2[r])
                    r+=1

                elif(r == n):
                    nums3.append(nums1[l])
                    l+=1

                elif (nums1[l] < nums2[r]):
                    nums3.append(nums1[l])
                    l+=1
            
                elif(nums1[l] >= nums2[r]):
                    nums3.append(nums2[r])
                    r+=1

        for i in range(len(nums3)):
            nums1[i] = nums3[i]
        

