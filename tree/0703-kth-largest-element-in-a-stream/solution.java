import java.util.PriorityQueue;

class KthLargest {

    private int k;
    private PriorityQueue<Integer> minHeap;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minHeap = new PriorityQueue<>();

        for (int num : nums) {
            add(num);
        }
    }

    public int add(int val) {

        minHeap.offer(val);

        // Keep only the k largest elements
        if (minHeap.size() > k) {
            minHeap.poll();
        }

        // Smallest element in heap = kth largest
        return minHeap.peek();
    }
}