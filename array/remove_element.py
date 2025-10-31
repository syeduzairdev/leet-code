from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0 
        for right in range(len(nums)):  
            if nums[right] != val:  
                nums[left] = nums[right]  
                left += 1  
        return left  


sol = Solution()
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = sol.removeElement(nums1, val1)
print(f"Test 1: k={k1}, nums[:k]={nums1[:k1]}")


nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = sol.removeElement(nums2, val2)
print(f"Test 2: k={k2}, nums[:k]={nums2[:k2]}")
