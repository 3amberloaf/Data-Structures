# Palidrome

1. Will never have more than O(n) iterations for the while loop because the pointers start n away from each other and move at least one step closer in every iteration
2. can be a linear runtime

# Example 1

* Initial thought was to interate overall pairs of integers (Brute Force Method) --> this would result in a time complexity of O(n^2)
* However since the array is SORTED we can achieve an O(n) time complexity
    1. Compare the first and last number together, if its too large then move the right pointer -1
    2. Re-compare to test the target number. If its too small, move the left pointer 1
    3. Continuously do this until target number is found
* Since the numbers are sorted, moving the left pointer permanently increases the value the left pointer points to (nums[left] = x).
* Similarly, moving the right pointer permanently decreases the value the right pointer points to (nums[right] = y). 
* We can manipulate the x and y variables in  `x + y > target`, to find the solution

# Example 2

* Since the two arrays are sorted, we SHOULD NOT just add them and resort
    - this would give a time complexity of O(n*logn)
    - would be a good approach if it was not sorted before
* In this example, to reach O(n) we should so `n = arr1.length + arr2.length` rather than `n = arr1.length and m = arr2.length`
    - O(n+m) vs O(n)
* time complexity of O(n) and space complexity of O(1)

# Example 3

* A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters
    - For example, "ace" is a subsequence of "abcde" while "aec" is not.
* If we find that s[i] == t[j], that means we "found" the letter at index i for s, and we can move on to the next one by incrementing i.
* s is a subsequence of t if we can "find" all the letters of s, which means that `i == s.length` at the end of the algorithm.

