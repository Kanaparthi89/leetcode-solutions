# 0115. Distinct Subsequences

**Difficulty:** Hard

**Tags:** String, Dynamic Programming

**Link:** https://leetcode.com/problems/distinct-subsequences/

---

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

&nbsp;
Example 1:


Input: s = &quot;rabbbit&quot;, t = &quot;rabbit&quot;
Output: 3
Explanation:
As shown below, there are 3 ways you can generate &quot;rabbit&quot; from s.
rabbbit
rabbbit
rabbbit


Example 2:


Input: s = &quot;babgbag&quot;, t = &quot;bag&quot;
Output: 5
Explanation:
As shown below, there are 5 ways you can generate &quot;bag&quot; from s.
babgbag
babgbag
babgbag
babgbag
babgbag

&nbsp;
Constraints:


	1 &lt;= s.length, t.length &lt;= 1000
	s and t consist of English letters.
