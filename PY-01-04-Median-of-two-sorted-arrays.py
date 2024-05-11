# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # If partitionX is 0, there is no left part for nums1, use -inf as maxLeftX
            # If partitionX is x, there is no right part for nums1, use +inf as minRightX
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If the total length is odd
                if (x + y) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                # If the total length is even
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

# Example usage:
# sol = Solution()
# result = sol.findMedianSortedArrays([1, 3, 8], [7, 9, 10, 11])
# print(result)  

######################################################################################################
#ALTERNATIVE 1>
######################################################################################################

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # If partitionX is 0, there is no left part for nums1, use -inf as maxLeftX
            # If partitionX is x, there is no right part for nums1, use +inf as minRightX
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If the total length is odd
                if (x + y) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                # If the total length is even
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

# Example usage:
# sol = Solution()
# result = sol.findMedianSortedArrays([1, 3, 8], [7, 9, 10, 11])
# print(result)  # Expected median might be around 8
