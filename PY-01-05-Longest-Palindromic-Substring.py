# A palindrome is a word, sentence, verse, or even number that reads the same backward or forward. 

# Given a string s, return the longest palindromic substring  in s.

# class Solution:
#     def longestPalindrome(self, s: str) -> str:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if not s:
            return ""
        
        longest_palindrome = ""
        for i in range(len(s)):
            # Case 1: The palindrome of odd length (one center)
            palindrome1 = expandAroundCenter(i, i)
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            
            # Case 2: The palindrome of even length (two centers)
            if i + 1 < len(s):
                palindrome2 = expandAroundCenter(i, i + 1)
                if len(palindrome2) > len(longest_palindrome):
                    longest_palindrome = palindrome2

        return longest_palindrome


solution = Solution()

input_string = "babad"

result = solution.longestPalindrome(input_string)

print("The longest palindromic substring is :", result)