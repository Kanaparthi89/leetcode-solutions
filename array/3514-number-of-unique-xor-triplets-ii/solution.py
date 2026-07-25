class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = list(set(nums))

        # pair[x] = True if x can be obtained as a XOR b
        pair = [False] * 2048
        for a in vals:
            for b in vals:
                pair[a ^ b] = True

        # trip[x] = True if x can be obtained as (a XOR b) XOR c
        trip = [False] * 2048
        for x in range(2048):
            if pair[x]:
                for c in vals:
                    trip[x ^ c] = True

        return sum(trip)