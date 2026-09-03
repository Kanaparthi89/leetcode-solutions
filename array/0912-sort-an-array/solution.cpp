class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        const int OFFSET = 50000;
        const int RANGE = 100001;

        vector<int> count(RANGE, 0);

        // Count frequency of each number
        for (int num : nums) {
            count[num + OFFSET]++;
        }

        // Reconstruct sorted array
        int index = 0;

        for (int i = 0; i < RANGE; i++) {
            while (count[i] > 0) {
                nums[index++] = i - OFFSET;
                count[i]--;
            }
        }

        return nums;
    }
};