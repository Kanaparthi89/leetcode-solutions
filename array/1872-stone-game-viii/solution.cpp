class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
        int n = stones.size();

        // prefix[i] = sum of stones[0 ... i-1]
        vector<long long> prefix(n + 1, 0);

        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] + stones[i - 1];
        }

        // If Alice takes all n stones, the difference is prefix[n].
        long long best = prefix[n];

        // Consider taking exactly i stones, where i >= 2.
        // Work backwards because best represents the opponent's
        // optimal result from the next state.
        for (int i = n - 1; i >= 2; i--) {
            best = max(best, prefix[i] - best);
        }

        return (int)best;
    }
};