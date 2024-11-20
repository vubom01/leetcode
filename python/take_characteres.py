# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/?envType=daily-question&envId=2024-11-20

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        cnt_chr = [0, 0, 0]

        for i in range(n):
            cnt_chr[ord(s[i]) - ord('a')] += 1

        if cnt_chr[0] < k or cnt_chr[1] < k or cnt_chr[2] < k:
            return -1

        result = n
        left, right = 0, 0
        while right < n:
            cnt_chr[ord(s[right]) - ord('a')] -= 1
            while left < n and (cnt_chr[0] < k or cnt_chr[1] < k or cnt_chr[2] < k):
                cnt_chr[ord(s[left]) - ord('a')] += 1
                left += 1
            result = min(result, left - 1 + n - right)
            right += 1
        return result

print(Solution().takeCharacters('ababaaccaa', 0))