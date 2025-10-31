from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0  # Non-val ke liye spot
        for right in range(len(nums)):  # Poora scan
            if nums[right] != val:  # Rakhne layak?
                nums[left] = nums[right]  # Left pe daal do
                left += 1  # Spot aage
        return left  # k ready

# Test 1: Example 1
sol = Solution()
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = sol.removeElement(nums1, val1)
print(f"Test 1: k={k1}, nums[:k]={nums1[:k1]}")

# Test 2: Example 2
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = sol.removeElement(nums2, val2)
print(f"Test 2: k={k2}, nums[:k]={nums2[:k2]}")