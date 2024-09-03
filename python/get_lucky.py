# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/?envType=daily-question&envId=2024-09-03

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = 0
        for c in s:
            val = ord(c) - ord('a') + 1
            while val > 0:
                number += val % 10
                val = int(val / 10)
        k -= 1
        while k > 0:
            newNumber = 0
            while number > 0:
                newNumber += number % 10
                number = int(number / 10)
            number = newNumber
            k -= 1

        return number


sol = Solution()
print(sol.getLucky("dbvmfhnttvr", 5))
