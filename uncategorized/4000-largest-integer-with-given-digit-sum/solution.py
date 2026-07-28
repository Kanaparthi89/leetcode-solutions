class Solution(object):
    def largestInteger(self, n, s):
        """
        :type n: int
        :type s: int
        :rtype: int
        """
        if s == 0:
            return 0

        if s > 9 * n:
            return -1

        digits = []

        for _ in range(n):
            digit = min(9, s)
            digits.append(str(digit))
            s -= digit

        return int("".join(digits))