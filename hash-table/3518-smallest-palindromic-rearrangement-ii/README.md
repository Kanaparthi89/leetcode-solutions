# 3518. Smallest Palindromic Rearrangement II

**Difficulty:** Hard

**Tags:** Hash Table, Math, String, Combinatorics, Counting

**Link:** https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

---

You are given a palindromic string s and an integer k.

Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

&nbsp;
Example 1:


Input: s = &quot;abba&quot;, k = 2

Output: &quot;baab&quot;

Explanation:


	The two distinct palindromic rearrangements of &quot;abba&quot; are &quot;abba&quot; and &quot;baab&quot;.
	Lexicographically, &quot;abba&quot; comes before &quot;baab&quot;. Since k = 2, the output is &quot;baab&quot;.



Example 2:


Input: s = &quot;aa&quot;, k = 2

Output: &quot;&quot;

Explanation:


	There is only one palindromic rearrangement: &quot;aa&quot;.
	The output is an empty string since k = 2 exceeds the number of possible rearrangements.



Example 3:


Input: s = &quot;bacab&quot;, k = 1

Output: &quot;abcba&quot;

Explanation:


	The two distinct palindromic rearrangements of &quot;bacab&quot; are &quot;abcba&quot; and &quot;bacab&quot;.
	Lexicographically, &quot;abcba&quot; comes before &quot;bacab&quot;. Since k = 1, the output is &quot;abcba&quot;.



&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 104
	s consists of lowercase English letters.
	s is guaranteed to be palindromic.
	1 &lt;= k &lt;= 106
