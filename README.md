# leetcode-exercises
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Approach 1: Brute Force
The brute force approach is simple. Loop through each element "x" and find if there is another value that equals to "target - x".
Complexity Analysis

Time complexity : $O(n^2)$. For each element, we try to find its complement by looping through the rest of array which takes $O(n)$ time. Therefore, the time complexity is $O(n^2)$.

Space complexity : $O(1)$.
