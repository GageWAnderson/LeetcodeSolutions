class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        sorted_intervals = sorted(
            intervals, key=lambda interval: interval[0]
        )  # O(nlogn)

        curr_interval_start = sorted_intervals[0][0]
        curr_interval_end = sorted_intervals[0][1]
        ans: List[List[int]] = []
        for j in range(1, len(sorted_intervals)):
            if sorted_intervals[j][0] <= curr_interval_end:
                curr_interval_end = max(sorted_intervals[j][1], curr_interval_end)
            else:
                ans.append([curr_interval_start, curr_interval_end])
                curr_interval_start = sorted_intervals[j][0]
                curr_interval_end = sorted_intervals[j][1]
        ans.append([curr_interval_start, curr_interval_end])
        return ans
