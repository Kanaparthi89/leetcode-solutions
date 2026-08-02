class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int n = s.length();

        // Try every possible substring length
        for (int len = 1; len <= n / 2; len++) {

            // The substring length must divide n
            if (n % len != 0) {
                continue;
            }

            boolean valid = true;

            // Compare each character with the repeating pattern
            for (int i = len; i < n; i++) {
                if (s.charAt(i) != s.charAt(i % len)) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                return true;
            }
        }

        return false;
    }
}
