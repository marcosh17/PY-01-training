class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Initialize variables
        s = s.lstrip()  # Remove leading whitespaces
        if not s:
            return 0
        
        sign = 1  # Default to positive sign
        index = 0
        result = 0
        length = len(s)
        
        # Step 2: Handle the sign if present
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        # Step 3: Convert the digits to an integer
        while index < length and s[index].isdigit():
            # Get the numeric value of the character
            result = result * 10 + (ord(s[index]) - ord('0'))
            index += 1
        
        # Step 4: Apply the sign
        result *= sign
        
        # Step 5: Handle overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        
        return result
