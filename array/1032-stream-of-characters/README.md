# 1032. Stream of Characters

**Difficulty:** Hard

**Tags:** Array, String, Design, Trie, Data Stream

**Link:** https://leetcode.com/problems/stream-of-characters/

---

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.

For example, if words = [&quot;abc&quot;, &quot;xyz&quot;]&nbsp;and the stream added the four characters (one by one) &#39;a&#39;, &#39;x&#39;, &#39;y&#39;, and &#39;z&#39;, your algorithm should detect that the suffix &quot;xyz&quot; of the characters &quot;axyz&quot; matches &quot;xyz&quot; from words.

Implement the StreamChecker class:


	StreamChecker(String[] words) Initializes the object with the strings array words.
	boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.


&nbsp;
Example 1:


Input
[&quot;StreamChecker&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;]
[[[&quot;cd&quot;, &quot;f&quot;, &quot;kl&quot;]], [&quot;a&quot;], [&quot;b&quot;], [&quot;c&quot;], [&quot;d&quot;], [&quot;e&quot;], [&quot;f&quot;], [&quot;g&quot;], [&quot;h&quot;], [&quot;i&quot;], [&quot;j&quot;], [&quot;k&quot;], [&quot;l&quot;]]
Output
[null, false, false, false, true, false, true, false, false, false, false, false, true]

Explanation
StreamChecker streamChecker = new StreamChecker([&quot;cd&quot;, &quot;f&quot;, &quot;kl&quot;]);
streamChecker.query(&quot;a&quot;); // return False
streamChecker.query(&quot;b&quot;); // return False
streamChecker.query(&quot;c&quot;); // return False
streamChecker.query(&quot;d&quot;); // return True, because &#39;cd&#39; is in the wordlist
streamChecker.query(&quot;e&quot;); // return False
streamChecker.query(&quot;f&quot;); // return True, because &#39;f&#39; is in the wordlist
streamChecker.query(&quot;g&quot;); // return False
streamChecker.query(&quot;h&quot;); // return False
streamChecker.query(&quot;i&
