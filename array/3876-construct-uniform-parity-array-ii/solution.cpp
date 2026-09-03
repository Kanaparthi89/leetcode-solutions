class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        bool hasOdd = false;
        bool hasEven = false;

        for (int x : nums1) {
            if (x % 2 == 0)
                hasEven = true;
            else
                hasOdd = true;
        }

        // Already uniform.
        if (!hasOdd || !hasEven)
            return true;

        // Mixed parity: the minimum element must be odd.
        int mn = *min_element(nums1.begin(), nums1.end());

        return mn % 2 == 1;
    }
};