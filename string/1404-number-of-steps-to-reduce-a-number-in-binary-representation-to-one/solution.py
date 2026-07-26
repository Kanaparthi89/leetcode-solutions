class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        carry = 0

        # Traverse from right to left, excluding the first bit
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry

            if bit == 1:
                # Odd: add 1, then divide by 2
                steps += 2
                carry = 1
            else:
                # Even: just divide by 2
                steps += 1

        return steps + carry