# 0831. Masking Personal Information

**Difficulty:** Medium

**Tags:** String

**Link:** https://leetcode.com/problems/masking-personal-information/

---

You are given a personal information string s, representing either an email address or a phone number. Return the masked personal information using the below rules.

Email address:

An email address is:


	A name consisting of at least two uppercase and lowercase English letters, followed by
	The &#39;@&#39; symbol, followed by
	The domain consisting of uppercase and lowercase English letters with a dot &#39;.&#39; somewhere in the middle (not the first or last character).


To mask an email:


	The uppercase letters in the name and domain must be converted to lowercase letters.
	The middle letters of the name (i.e., all but the first and last letters) must be replaced by 5 asterisks &quot;*****&quot;.


Phone number:

A phone number is formatted as follows:


	The phone number contains 10-13 digits.
	The last 10 digits make up the local number.
	The remaining 0-3 digits, in the beginning, make up the country code.
	Separation characters from the set {&#39;+&#39;, &#39;-&#39;, &#39;(&#39;, &#39;)&#39;, &#39; &#39;} separate the above digits in some way.


To mask a phone number:


	Remove all separation characters.
	The masked phone number should have the form:
	
		&quot;***-***-XXXX&quot; if the country code has 0 digits.
		&quot;+*-***-***-XXXX&quot; if the country code has 1 digit.
		&quot;+**-***-***-XXXX&quot; if the country code has 2 digits.
		&quot;+***-***-***-XXXX&quot; if the country code has 3 digits.
	
	
	&quot;XXXX&quot; is the last 4 digits of the local number.


&nbsp;
Example 1:


Input: s = &quot;LeetCode@LeetCode.com&quot;
Output: &quot;l*****e@leetcode.com&quot;
Explanation: s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.


Example 2:


Input: s = &quot;AB@qq.com&quot;
Output: &quot;a*****b@qq.com&quot;
Explanation: s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
Note that even though &quot;ab
