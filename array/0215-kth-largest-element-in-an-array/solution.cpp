class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int target = nums.size() - k;

        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            // Random pivot
            int pivotIndex = left + rand() % (right - left + 1);
            int pivot = nums[pivotIndex];

            // 3-way partition:
            // [left ... low-1]   < pivot
            // [low ... high]     == pivot
            // [high+1 ... right] > pivot

            int low = left;
            int high = right;
            int i = left;

            while (i <= high) {
                if (nums[i] < pivot) {
                    swap(nums[i], nums[low]);
                    i++;
                    low++;
                }
                else if (nums[i] > pivot) {
                    swap(nums[i], nums[high]);
                    high--;
                }
                else {
                    i++;
                }
            }

            // target is in the < pivot section
            if (target < low) {
                right = low - 1;
            }
            // target is in the > pivot section
            else if (target > high) {
                left = high + 1;
            }
            // target is inside == pivot section
            else {
                return pivot;
            }
        }

        return -1;
    }
};