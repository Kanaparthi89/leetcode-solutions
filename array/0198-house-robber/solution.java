class Solution {
    public int rob(int[] nums) {

        int prev2 = 0; // Maximum before previous house
        int prev1 = 0; // Maximum up to previous house

        for (int money : nums) {

            int current = Math.max(
                prev1,           // Don't rob this house
                prev2 + money   // Rob this house
            );

            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}