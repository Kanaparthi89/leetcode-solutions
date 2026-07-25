# 3514. Number of Unique XOR Triplets II

**Difficulty:** Medium

**Tags:** Array, Math, Bit Manipulation, Enumeration

**Link:** https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

---

You are given an integer array nums.

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i &lt;= j &lt;= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).

&nbsp;
Example 1:


Input: nums = [1,3]

Output: 2

Explanation:

The possible XOR triplet values are:


	(0, 0, 0) &rarr; 1 XOR 1 XOR 1 = 1
	(0, 0, 1) &rarr; 1 XOR 1 XOR 3 = 3
	(0, 1, 1) &rarr; 1 XOR 3 XOR 3 = 1
	(1, 1, 1) &rarr; 3 XOR 3 XOR 3 = 3


The unique XOR values are {1, 3}. Thus, the output is 2.


Example 2:


Input: nums = [6,7,8,9]

Output: 4

Explanation:

The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 1500
	1 &lt;= nums[i] &lt;= 1500
