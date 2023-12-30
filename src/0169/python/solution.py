from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x, count = -1, 0

        for num in nums:
            if count == 0:
                x = num
            count += 1 if num == x else -1

        return x
