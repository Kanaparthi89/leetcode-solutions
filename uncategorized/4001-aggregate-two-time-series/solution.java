class Solution {
    public List<List<Integer>> aggregateTimeSeries(int[][] series1, int[][] series2) {
        List<List<Integer>> ans = new ArrayList<>();

        int i = 0, j = 0;

        while (i < series1.length || j < series2.length) {
            int t;

            if (j == series2.length || (i < series1.length && series1[i][0] < series2[j][0])) {
                t = series1[i][0];
            } else if (i == series1.length || series2[j][0] < series1[i][0]) {
                t = series2[j][0];
            } else {
                t = series1[i][0];
            }

            long v1 = (i < series1.length) ? series1[i][1] : 0;
            long v2 = (j < series2.length) ? series2[j][1] : 0;

            ans.add(Arrays.asList(t, (int)(v1 + v2)));

            if (i < series1.length && series1[i][0] == t) {
                i++;
            }
            if (j < series2.length && series2[j][0] == t) {
                j++;
            }
        }

        return ans;
    }
}