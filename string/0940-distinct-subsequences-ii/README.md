# 0940. Distinct Subsequences II

**Difficulty:** Hard

**Tags:** String, Dynamic Programming

**Link:** https://leetcode.com/problems/distinct-subsequences-ii/

---

Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., &quot;ace&quot; is a subsequence of &quot;abcde&quot; while &quot;aec&quot; is not.
&nbsp;
Example 1:


Input: s = &quot;abc&quot;
Output: 7
Explanation: The 7 distinct subsequences are &quot;a&quot;, &quot;b&quot;, &quot;c&quot;, &quot;ab&quot;, &quot;ac&quot;, &quot;bc&quot;, and &quot;abc&quot;.


Example 2:


Input: s = &quot;aba&quot;
Output: 6
Explanation: The 6 distinct subsequences are &quot;a&quot;, &quot;b&quot;, &quot;ab&quot;, &quot;aa&quot;, &quot;ba&quot;, and &quot;aba&quot;.


Example 3:


Input: s = &quot;aaa&quot;
Output: 3
Explanation: The 3 distinct subsequences are &quot;a&quot;, &quot;aa&quot; and &quot;aaa&quot;.


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 2000
	s consists of lowercase English letters.
