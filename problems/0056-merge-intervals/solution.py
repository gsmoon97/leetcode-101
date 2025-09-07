class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # keep track of running_start, running_end
        # only flush when running_end < current_start
        # otherwise keep updating the running_end
        merged_intervals = []
        running_start, running_end = intervals[0]
        for curr_start, curr_end in intervals[1:]:
            if curr_start <= running_end:  # if overlapping, extend the running interval
                running_end = max(running_end, curr_end)
            else:  # if non-overalpping, save the current and start a new interval
                merged_intervals.append([running_start, running_end])
                running_start, running_end = curr_start, curr_end
        merged_intervals.append([running_start, running_end])  # flush the remaining interval
        return merged_intervals
