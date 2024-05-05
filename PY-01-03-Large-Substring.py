# Given a string s, find the length of the longest substring  without repeating characters.

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_len = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            char_map[char] = i
            max_len = max(max_len, i - start + 1)

        return max_len
    
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
