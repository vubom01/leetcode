"""
https://leetcode.com/problems/reverse-words-in-a-string/description/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = list(reversed(words))
        return " ".join(words)


sol = Solution()
print(sol.reverseWords("a good   example"))
