# 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target

**Difficulty:** Hard

**Tags:** Two Pointers, String, Enumeration

**Link:** https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

---

You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

&nbsp;
Example 1:


Input: s = &quot;baba&quot;, target = &quot;abba&quot;

Output: &quot;baab&quot;

Explanation:


	The palindromic permutations of s (in lexicographical order) are &quot;abba&quot; and &quot;baab&quot;.
	The lexicographically smallest permutation that is strictly greater than target is &quot;baab&quot;.



Example 2:


Input: s = &quot;baba&quot;, target = &quot;bbaa&quot;

Output: &quot;&quot;

Explanation:


	The palindromic permutations of s (in lexicographical order) are &quot;abba&quot; and &quot;baab&quot;.
	None of them is lexicographically strictly greater than target. Therefore, the answer is &quot;&quot;.



Example 3:


Input: s = &quot;abc&quot;, target = &quot;abb&quot;

Output: &quot;&quot;

Explanation:

s has no palindromic permutations. Therefore, the answer is &quot;&quot;.


Example 4:


Input: s = &quot;aac&quot;, target = &quot;abb&quot;

Output: &quot;aca&quot;

Explanation:


	The only palindromic permutation of s is &quot;aca&quot;.
	&quot;aca&quot; is strictly greater than target. Therefore, the answer is &quot;aca&quot;.



&nbsp;
Constraints:


	1 &lt;= n == s.length == target.length &lt;= 300
	s and target consist of only lowercase English letters.
