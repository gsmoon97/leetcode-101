class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Given two lines, the volume is constrained by the height of the shorter line.
        # Intution is to replace the shorter line with a longer line, but the increase in height (i.e., y-axis) should be greater than the decrease in width (i.e., x-axis) for the replacement to result in larger volume
        # Implement this heuristics using two pointers
        # May not always guarantee the largest volume, so could try out shifting the shorter line by one (regardless of the height of the new line) and keeping track of the maximum volume instead.
        start, end = 0, len(height) - 1
        max_volume = -1
        while start < end:
            start_h = height[start]
            end_h = height[end]
            volume = min(start_h, end_h) * (end - start)  # height x width
            max_volume = max(max_volume, volume)
            if start_h < end_h:
                start += 1
            else:
                end -= 1
        return max_volume
