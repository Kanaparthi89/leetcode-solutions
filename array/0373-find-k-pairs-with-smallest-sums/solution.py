import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        result = []
        min_heap = []

        # Put first pair of each nums1 element with nums2[0]
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while min_heap and len(result) < k:
            _, i, j = heapq.heappop(min_heap)

            result.append([nums1[i], nums2[j]])

            # Move to next element in nums2 for the same nums1[i]
            if j + 1 < len(nums2):
                heapq.heappush(
                    min_heap,
                    (nums1[i] + nums2[j + 1], i, j + 1)
                )

        return result