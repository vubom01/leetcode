"""
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t = ""
        for c in s:
            t = t + str(ord(c) - 96)
        for _ in range(k):
            s = 0
            for i in t:
                s += int(i)
            t = str(s)
        return int(t)


sol = Solution()
print(sol.getLucky("iiii", 1))
