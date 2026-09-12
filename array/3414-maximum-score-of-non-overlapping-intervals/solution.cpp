class Solution {
public:
    struct Node {
        long long score;
        vector<int> ids;
    };

    bool better(const Node& a, const Node& b) {
        if (a.score != b.score)
            return a.score > b.score;

        return a.ids < b.ids;
    }

    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();

        // {left, right, weight, original index}
        vector<array<long long, 4>> a(n);

        for (int i = 0; i < n; i++) {
            a[i] = {
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            };
        }

        // Sort by starting position
        sort(a.begin(), a.end(), [](const auto& x, const auto& y) {
            if (x[0] != y[0])
                return x[0] < y[0];
            return x[1] < y[1];
        });

        vector<long long> starts(n);
        for (int i = 0; i < n; i++)
            starts[i] = a[i][0];

        // next[i] = first interval whose left > a[i].right
        vector<int> next(n);

        for (int i = 0; i < n; i++) {
            next[i] = upper_bound(
                starts.begin(),
                starts.end(),
                a[i][1]
            ) - starts.begin();
        }

        // dp[i][k] = best answer using intervals i...n-1
        // with at most k intervals.
        vector<array<Node, 5>> dp(n + 1);

        // Base case: no intervals left
        for (int k = 0; k <= 4; k++) {
            dp[n][k] = {0, {}};
        }

        for (int i = n - 1; i >= 0; i--) {
            // With 0 intervals allowed, choose nothing.
            dp[i][0] = {0, {}};

            for (int k = 1; k <= 4; k++) {

                // Option 1: skip this interval
                Node skip = dp[i + 1][k];

                // Option 2: take this interval
                Node take = dp[next[i]][k - 1];

                take.score += a[i][2];
                take.ids.push_back((int)a[i][3]);

                // Keep indices sorted because the final answer
                // must be compared lexicographically.
                sort(take.ids.begin(), take.ids.end());

                if (better(take, skip))
                    dp[i][k] = take;
                else
                    dp[i][k] = skip;
            }
        }

        return dp[0][4].ids;
    }
};