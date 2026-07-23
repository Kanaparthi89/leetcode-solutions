class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.size();
        int totalOnes = 0;
        for (char c : s) if (c == '1') totalOnes++;

        vector<array<int,3>> groups;
        int i = 0;
        while (i < n) {
            int j = i;
            while (j + 1 < n && s[j + 1] == s[i]) j++;
            groups.push_back({i, j, s[i] - '0'});
            i = j + 1;
        }

        int gsz = groups.size();
        vector<int> A, B, LS, RE, full;
        for (int gi = 0; gi < gsz; gi++) {
            if (groups[gi][2] != 1) continue;
            if (gi == 0 || gi == gsz - 1) continue;
            int a = groups[gi][0], b = groups[gi][1];
            int ls = groups[gi - 1][0];
            int re = groups[gi + 1][1];
            A.push_back(a);
            B.push_back(b);
            LS.push_back(ls);
            RE.push_back(re);
            full.push_back((a - ls) + (re - b));
        }

        int m = A.size();
        int LOG = 1;
        while ((1 << LOG) <= max(m, 1)) LOG++;
        vector<vector<int>> sparse;
        if (m > 0) {
            sparse.assign(LOG, vector<int>(m));
            sparse[0] = full;
            for (int k = 1; k < LOG; k++) {
                int half = 1 << (k - 1);
                for (int idx = 0; idx + (1 << k) <= m; idx++) {
                    sparse[k][idx] = max(sparse[k - 1][idx], sparse[k - 1][idx + half]);
                }
            }
        }

        auto rangeMax = [&](int l, int r) -> long long {
            if (l > r) return LLONG_MIN;
            int k = 31 - __builtin_clz(r - l + 1);
            return max(sparse[k][l], sparse[k][r - (1 << k) + 1]);
        };

        int q = queries.size();
        vector<int> ans(q, 0);

        for (int qi = 0; qi < q; qi++) {
            int l = queries[qi][0];
            int r = queries[qi][1];
            long long gain = 0;

            if (m > 0) {
                int lo = upper_bound(A.begin(), A.end(), l) - A.begin();
                int cnt = lower_bound(B.begin(), B.end(), r) - B.begin();
                int hi = cnt - 1;

                if (lo <= hi && lo < m && hi >= 0) {
                    if (lo == hi) {
                        long long left = A[lo] - max(LS[lo], l);
                        long long right = min(RE[lo], r) - B[lo];
                        gain = max(gain, left + right);
                    } else {
                        long long gainLo = (A[lo] - max(LS[lo], l)) + (RE[lo] - B[lo]);
                        long long gainHi = (A[hi] - LS[hi]) + (min(RE[hi], r) - B[hi]);
                        gain = max(gain, gainLo);
                        gain = max(gain, gainHi);
                        if (lo + 1 <= hi - 1) {
                            long long mid = rangeMax(lo + 1, hi - 1);
                            gain = max(gain, mid);
                        }
                    }
                }
            }

            ans[qi] = totalOnes + (int)gain;
        }

        return ans;
    }
};