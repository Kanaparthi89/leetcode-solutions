import java.util.*;

class SummaryRanges {

    // start -> end
    private TreeMap<Integer, Integer> map;

    public SummaryRanges() {
        map = new TreeMap<>();
    }

    public void addNum(int value) {

        // Find interval with the largest start <= value
        Map.Entry<Integer, Integer> prev = map.floorEntry(value);

        // Already covered by an existing interval
        if (prev != null && prev.getValue() >= value) {
            return;
        }

        // Find interval with the smallest start >= value
        Map.Entry<Integer, Integer> next = map.ceilingEntry(value);

        boolean connectPrev = prev != null && prev.getValue() + 1 == value;
        boolean connectNext = next != null && value + 1 == next.getKey();

        if (connectPrev && connectNext) {
            // Merge previous and next intervals
            int prevStart = prev.getKey();
            int nextEnd = next.getValue();

            map.put(prevStart, nextEnd);
            map.remove(next.getKey());

        } else if (connectPrev) {
            // Extend previous interval
            map.put(prev.getKey(), value);

        } else if (connectNext) {
            // Extend next interval backward
            int nextEnd = next.getValue();

            map.remove(next.getKey());
            map.put(value, nextEnd);

        } else {
            // Create a new interval
            map.put(value, value);
        }
    }

    public int[][] getIntervals() {

        int[][] result = new int[map.size()][2];

        int i = 0;

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            result[i][0] = entry.getKey();
            result[i][1] = entry.getValue();
            i++;
        }

        return result;
    }
}