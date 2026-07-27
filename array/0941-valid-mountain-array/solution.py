class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        
        # Mountain array must have at least 3 elements
        if n < 3:
            return False
        
        i = 0
        
        # Go up
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1
        
        # Peak cannot be first or last
        if i == 0 or i == n - 1:
            return False
        
        # Go down
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        
        # Valid if we reached the end
        return i == n - 1