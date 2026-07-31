import java.util.*;

class Solution {
    public int minimumPushes(String word) {
        int[] freq = new int[26];

        // Count frequency of each letter
        for (char c : word.toCharArray()) {
            freq[c - 'a']++;
        }

        // Sort frequencies in descending order
        Arrays.sort(freq);

        int pushes = 0;
        int cost = 1;

        // Process from highest frequency to lowest
        for (int i = 25; i >= 0; i--) {
            if (freq[i] == 0) {
                continue;
            }

            // Every 8 letters, the required pushes increase
            cost = (25 - i) / 8 + 1;

            pushes += freq[i] * cost;
        }

        return pushes;
    }
}