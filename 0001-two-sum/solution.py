from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}  # value -> index

        for i, num in enumerate(nums):
            j = seen.get(target - num)  # index of complement if present
            if j is not None:
                return [j, i]  # earlier index first
            seen[num] = i  # store the current value

        # Problem guarantees a solution, but good practice:
        raise ValueError("No two sum solution")
