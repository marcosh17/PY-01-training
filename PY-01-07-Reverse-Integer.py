# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        
        reversed_num = int(str(abs(x))[::-1])
        
        # Restore the sign
        reversed_num *= sign
        
        # Check if the reversed number is within the 32-bit integer range
        if reversed_num < MIN_INT or reversed_num > MAX_INT:
            return 0
        
        return reversed_num
