class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // Sort by starting point
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> result;

        // Start with the first interval
        result.push_back(intervals[0]);

        for (int i = 1; i < intervals.size(); i++) {
            int currentStart = intervals[i][0];
            int currentEnd = intervals[i][1];

            int& lastStart = result.back()[0];
            int& lastEnd = result.back()[1];

            // Overlapping intervals
            if (currentStart <= lastEnd) {
                lastEnd = max(lastEnd, currentEnd);
            }
            // No overlap
            else {
                result.push_back(intervals[i]);
            }
        }

        return result;
    }
};