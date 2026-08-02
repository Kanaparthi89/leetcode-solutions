# 0686. Repeated String Match

**Difficulty:** Medium

**Tags:** String, String Matching

**Link:** https://leetcode.com/problems/repeated-string-match/

---

Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string &quot;abc&quot; repeated 0 times is &quot;&quot;, repeated 1 time is &quot;abc&quot; and repeated 2 times is &quot;abcabc&quot;.

&nbsp;
Example 1:


Input: a = &quot;abcd&quot;, b = &quot;cdabcdab&quot;
Output: 3
Explanation: We return 3 because by repeating a three times &quot;abcdabcdabcd&quot;, b is a substring of it.


Example 2:


Input: a = &quot;a&quot;, b = &quot;aa&quot;
Output: 2


&nbsp;
Constraints:


	1 &lt;= a.length, b.length &lt;= 104
	a and b consist of lowercase English letters.
