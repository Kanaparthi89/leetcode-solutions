# 3720. Lexicographically Smallest Permutation Greater Than Target

**Difficulty:** Medium

**Tags:** Hash Table, String, Greedy, Counting, Enumeration

**Link:** https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

---

You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

&nbsp;
Example 1:


Input: s = &quot;abc&quot;, target = &quot;bba&quot;

Output: &quot;bca&quot;

Explanation:


	The permutations of s (in lexicographical order) are &quot;abc&quot;, &quot;acb&quot;, &quot;bac&quot;, &quot;bca&quot;, &quot;cab&quot;, and &quot;cba&quot;.
	The lexicographically smallest permutation that is strictly greater than target is &quot;bca&quot;.



Example 2:


Input: s = &quot;leet&quot;, target = &quot;code&quot;

Output: &quot;eelt&quot;

Explanation:


	The permutations of s (in lexicographical order) are &quot;eelt&quot;, &quot;eetl&quot;, &quot;elet&quot;, &quot;elte&quot;, &quot;etel&quot;, &quot;etle&quot;, &quot;leet&quot;, &quot;lete&quot;, &quot;ltee&quot;, &quot;teel&quot;, &quot;tele&quot;, and &quot;tlee&quot;.
	The lexicographically smallest permutation that is strictly greater than target is &quot;eelt&quot;.



Example 3:


Input: s = &quot;baba&quot;, target = &quot;bbaa&quot;

Output: &quot;&quot;

Explanation:


	The permutations of s (in lexicographical order) are &quot;aabb&quot;, &quot;abab&quot;, &quot;abba&quot;, &quot;baab&quot;, &quot;baba&quot;, and &quot;bbaa&quot;.
	None of them is lexicographically strictly greater than target. Therefore, the answer is &quot;&quot;.



&nbsp;
Constraints:


	1 &lt;= s.length == target.length &lt;= 300
	s and target consist of only lowercase English letters.
