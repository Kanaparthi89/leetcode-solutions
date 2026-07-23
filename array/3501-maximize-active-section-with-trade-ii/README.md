# 3501. Maximize Active Section with Trade II

**Difficulty:** Hard

**Tags:** Array, String, Binary Search, Segment Tree

**Link:** https://leetcode.com/problems/maximize-active-section-with-trade-ii/

---

You are given a binary string s of length n, where:


	&#39;1&#39; represents an active section.
	&#39;0&#39; represents an inactive section.


You can perform at most one trade to maximize the number of active sections in s. In a trade, you:


	Convert a contiguous block of &#39;1&#39;s that is surrounded by &#39;0&#39;s to all &#39;0&#39;s.
	Afterward, convert a contiguous block of &#39;0&#39;s that is surrounded by &#39;1&#39;s to all &#39;1&#39;s.


Additionally, you are given a 2D array queries, where queries[i] = [li, ri] represents a substring s[li...ri].

For each query, determine the maximum possible number of active sections in s after making the optimal trade on the substring s[li...ri].

Return an array answer, where answer[i] is the result for queries[i].

Note


	For each query, treat s[li...ri] as if it is augmented with a &#39;1&#39; at both ends, forming t = &#39;1&#39; + s[li...ri] + &#39;1&#39;. The augmented &#39;1&#39;s do not contribute to the final count.
	The queries are independent of each other.


&nbsp;
Example 1:


Input: s = &quot;01&quot;, queries = [[0,1]]

Output: [1]

Explanation:

Because there is no block of &#39;1&#39;s surrounded by &#39;0&#39;s, no valid trade is possible. The maximum number of active sections is 1.


Example 2:


Input: s = &quot;0100&quot;, queries = [[0,3],[0,2],[1,3],[2,3]]

Output: [4,3,1,1]

Explanation:


	
	Query [0, 3] &rarr; Substring &quot;0100&quot; &rarr; Augmented to &quot;101001&quot;
	Choose &quot;0100&quot;, convert &quot;0100&quot; &rarr; &quot;0000&quot; &rarr; &quot;1111&quot;.
	The final string without augmentation is &quot;1111&quot;. The maximum number of active sections is 4.
	
	
	Query [0, 2] &rarr; Substring &quot;010&quot; &rarr; Augmented to &quot;10101&quot;
	Choose &quot;010&quot;, convert &quot;010&quot; &rarr; &quot;000&quot; &rarr; &quot;111&quot;.
	The final string without augmentation is &quot;1110&quot;. The maximum number of active sections is 3.
	
	
	Query [1, 3] &rarr; Subs
