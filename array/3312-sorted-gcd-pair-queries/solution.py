from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for m in range(g, mx + 1, g):
                cnt[g] += freq[m]

        exact = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            pairs = cnt[g] * (cnt[g] - 1) // 2
            m = 2 * g
            while m <= mx:
                pairs -= exact[m]
                m += g
            exact[g] = pairs

        prefix = []
        values = []
        total = 0
        for g in range(1, mx + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        ans = []
        for q in queries:
            ans.append(values[bisect_right(prefix, q)])

        return ans