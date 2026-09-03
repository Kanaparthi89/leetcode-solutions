# 3568. Minimum Moves to Clean the Classroom

**Difficulty:** Medium

**Tags:** Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix

**Link:** https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

---

You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:


	&#39;S&#39;: Starting position of the student
	&#39;L&#39;: Litter that must be collected (once collected, the cell becomes empty)
	&#39;R&#39;: Reset area that restores the student&#39;s energy to full capacity, regardless of their current energy level (can be used multiple times)
	&#39;X&#39;: Obstacle the student cannot pass through
	&#39;.&#39;: Empty space


You are also given an integer energy, representing the student&#39;s maximum energy capacity. The student starts with this energy from the starting position &#39;S&#39;.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area &#39;R&#39;, which resets the energy to its maximum capacity energy.

Return the minimum number of moves required to collect all litter items, or -1 if it&#39;s impossible.

&nbsp;
Example 1:


Input: classroom = [&quot;S.&quot;, &quot;XL&quot;], energy = 2

Output: 2

Explanation:


	The student starts at cell (0, 0) with 2 units of energy.
	Since cell (1, 0) contains an obstacle &#39;X&#39;, the student cannot move directly downward.
	A valid sequence of moves to collect all litter is as follows:
	
		Move 1: From (0, 0) &rarr; (0, 1) with 1 unit of energy and 1 unit remaining.
		Move 2: From (0, 1) &rarr; (1, 1) to collect the litter &#39;L&#39;.
	
	
	The student collects all the litter using 2 moves. Thus, the output is 2.



Example 2:


Input: classroom = [&quot;LS&quot;, &quot;RL&quot;], energy = 4

Output: 3

Explanation:


	The student starts at cell (0, 1) with 4 units of energy.
	A valid sequence of moves to collect all litter is as follows:
	
		Move 1: From (0, 1) &rarr; (0, 0) to collect the first litter &#39;L&#39; with 1 unit of energy used and 3 units remaining.
		Move 2: From (0, 0) &rarr; (
