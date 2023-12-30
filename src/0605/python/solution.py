from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0 if flowerbed[0] else 1

        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)  # int division, round toward zero
                empty = 0
            else:
                empty += 1

        n -= (empty) // 2  # floor division, round down
        return n <= 0
