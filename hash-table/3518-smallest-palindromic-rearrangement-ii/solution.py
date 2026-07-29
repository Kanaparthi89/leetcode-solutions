from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        freq = Counter(s)

        half = [0] * 26
        mid = ""
        length = 0

        for ch, cnt in freq.items():
            if cnt % 2:
                mid = ch
            half[ord(ch) - ord('a')] = cnt // 2
            length += cnt // 2

        LIMIT = k

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - r + i) // i
                if res > LIMIT:
                    return LIMIT + 1
            return res

        def countWays(cnt):
            rem = sum(cnt)
            ans = 1
            left = rem
            for c in cnt:
                if c:
                    ans *= comb(left, c)
                    if ans > LIMIT:
                        return LIMIT + 1
                    left -= c
            return ans

        if countWays(half) < k:
            return ""

        first = []

        for _ in range(length):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = countWays(half)

                if ways >= k:
                    first.append(chr(i + ord('a')))
                    break
                else:
                    k -= ways
                    half[i] += 1

        first = "".join(first)
        return first + mid + first[::-1]
        