# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
        
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Base cases where no zigzag pattern is necessary
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Rows to hold each level of characters
        rows = [''] * numRows
        current_row = 0
        going_down = False  # Direction flag
        
        # Populate rows with the appropriate characters
        for char in s:
            rows[current_row] += char
            # Determine if we need to go down or up
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        
        # Concatenate all rows to form the final string
        return ''.join(rows)

# # Example usage:
# sol = Solution()
# result = sol.convert("PAYPALISHIRING", 3)
# print(result)  # Output should be "PAHNAPLSIIGYIR"
