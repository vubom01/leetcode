# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/description/

from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        minProd = -10000000000
        maxProd = 10000000000
        res = maxProd

        positiveNums1, negativeNums1 = [], []
        for idx, num in enumerate(nums1):
            if num >= 0:
                positiveNums1.append(num)
            else:
                negativeNums1.append(num)

        positiveNums2, negativeNums2 = [], []
        for idx, num in enumerate(nums2):
            if num >= 0:
                positiveNums2.append(num)
            else:
                negativeNums2.append(num)

        while minProd <= maxProd:
            prod = (minProd + maxProd) // 2
            counter = 0

            if prod < 0:
                right = len(positiveNums2) - 1
                prev = 0
                for num in reversed(negativeNums1):
                    while right >= 0 and num * positiveNums2[right] <= prod:
                        right -= 1
                        prev += 1
                    counter += prev

                left = 0
                prev = 0
                for num in positiveNums1:
                    if num == 0:
                        continue
                    while left < len(negativeNums2) and num * negativeNums2[left] <= prod:
                        left += 1
                        prev += 1
                    counter += prev
            else:
                counter += len(positiveNums1) * len(negativeNums2) + len(negativeNums1) * len(positiveNums2)
                right = len(negativeNums2) - 1
                prev = 0
                for num in negativeNums1:
                    while right >= 0 and num * negativeNums2[right] <= prod:
                        right -= 1
                        prev += 1
                    counter += prev

                left = 0
                prev = 0
                for num in reversed(positiveNums1):
                    while left < len(positiveNums2) and num * positiveNums2[left] <= prod:
                        left += 1
                        prev += 1
                    counter += prev

            if counter >= k:
                res = prod
                maxProd = prod - 1
            else:
                minProd = prod + 1
        return res


sol = Solution()
print(sol.kthSmallestProduct([-4, -2, 0, 3], [2, 4], 6))
print(sol.kthSmallestProduct([2, 5], [3, 4], 2))
print(sol.kthSmallestProduct([-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3))
print(sol.kthSmallestProduct([-9, 6, 10], [-7, -1, 1, 2, 3, 4, 4, 6, 9, 10], 15))
print(sol.kthSmallestProduct([-9, -4, 1, 6, 8, 8, 9, 10], [-10, -10, -8, -8, 1, 3, 6, 6, 8, 10], 29))
