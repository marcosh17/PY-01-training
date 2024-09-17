class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If the number is negative or ends in 0 (except if the number is 0), it is not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_half = 0
        while x > reverted_half:
            # Take the last digit of x and add it to reverted_half
            reverted_half = reverted_half * 10 + x % 10
            # Remove the last digit from x
            x //= 10
        
        # The number is a palindrome if x is equal to the reverted half,
        # or if x is equal to reverted_half // 10
        return x == reverted_half or x == reverted_half // 10

