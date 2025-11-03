from typing import List
"""
Linear search implementation for search insert position.
Note: This runs in O(n) time, not O(log n) as required by the problem.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       for i in range(len(nums)):
            if nums[i] >= target:
                return i
       return len(nums)




        
sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))  # expected: 2
print(sol.searchInsert([1,3,5,6], 7))  # expected: 2