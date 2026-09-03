class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.size();

        // Count characters available from s
        vector<int> cnt(26, 0);
        for (char c : s) {
            cnt[c - 'a']++;
        }

        // We try to make the prefix equal to target.
        // If at position i we can choose something greater,
        // that is a candidate answer.
        for (int i = n - 1; i >= 0; i--) {
            // Reconstruct characters used by target[0..i-1]
            vector<int> cur = cnt;
            bool possible = true;

            for (int j = 0; j < i; j++) {
                int x = target[j] - 'a';

                if (cur[x] == 0) {
                    possible = false;
                    break;
                }

                cur[x]--;
            }

            if (!possible) continue;

            // At position i, choose the smallest character
            // strictly greater than target[i].
            int x = target[i] - 'a';

            for (int c = x + 1; c < 26; c++) {
                if (cur[c] > 0) {
                    string ans = target.substr(0, i);
                    ans += char('a' + c);
                    cur[c]--;

                    // Fill remaining positions with smallest chars
                    for (int k = 0; k < 26; k++) {
                        while (cur[k] > 0) {
                            ans += char('a' + k);
                            cur[k]--;
                        }
                    }

                    return ans;
                }
            }
        }

        return "";
    }
};