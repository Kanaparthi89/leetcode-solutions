class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int left = 0;
        int right = arr.size() - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] < arr[mid + 1]) {
                // We are on the increasing side
                // Peak is to the right
                left = mid + 1;
            } else {
                // We are on the decreasing side
                // Peak is at mid or to the left
                right = mid;
            }
        }

        return left;
    }
};