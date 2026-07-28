import java.util.*;

class Solution {
    public boolean isPossible(int[] target) {
        PriorityQueue<Long> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        long sum = 0;

        for (int num : target) {
            maxHeap.offer((long) num);
            sum += num;
        }

        while (true) {
            long largest = maxHeap.poll();

            if (largest == 1) {
                return true;
            }

            long rest = sum - largest;

            // Cannot reduce a single element greater than 1
            if (rest == 0) {
                return false;
            }

            // If all other elements are 1, we can always reach 1
            if (rest == 1) {
                return true;
            }

            long previous = largest % rest;

            // Means it cannot be reduced to a valid positive value
            if (previous == 0 || previous == largest) {
                return false;
            }

            maxHeap.offer(previous);
            sum = rest + previous;
        }
    }
}