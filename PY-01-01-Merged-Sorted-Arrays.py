# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 
# and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of 
# m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a 
# length of n. 

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0 and i >= 0:
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        # If there are elements left in nums2 that must be copied
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Example of use

# sol = Solution()
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# sol.merge(nums1, 3, nums2, 3)
# print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
