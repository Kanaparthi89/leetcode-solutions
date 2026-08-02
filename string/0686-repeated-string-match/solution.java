class Solution {
    public int repeatedStringMatch(String a, String b) {

        StringBuilder repeated = new StringBuilder();

        int count = 0;

        // Repeat until the length is at least b.length()
        while (repeated.length() < b.length()) {
            repeated.append(a);
            count++;
        }

        // Check with the current number of repetitions
        if (repeated.toString().contains(b)) {
            return count;
        }

        // One additional repetition may be needed
        repeated.append(a);
        count++;

        if (repeated.toString().contains(b)) {
            return count;
        }

        return -1;
    }
}