class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int operations = 0;
        int distinctSmaller = 0;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i - 1]) {
                distinctSmaller++;
            }

            operations += distinctSmaller;
        }

        return operations;
    }
};