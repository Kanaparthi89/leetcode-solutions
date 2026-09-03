class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        bool hasOdd = false;
        bool hasEven = false;

        for (int x : nums1) {
            if (x % 2)
                hasOdd = true;
            else
                hasEven = true;
        }

        // If all are already the same parity
        if (!hasOdd || !hasEven)
            return true;

        // If both exist, use an odd number as the subtraction partner:
        // odd - odd = even
        // even - odd = odd
        //
        // We can choose the target parity appropriately.
        return true;
    }
};