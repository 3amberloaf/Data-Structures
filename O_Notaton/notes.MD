# Big O

Big O notation described the computational complexity of an algorithm via:

    - time complexity
    - space complexity

N is the input size.

## Examples

* O(n)
* O(n^2)
* O(2^n)
* O(log n)
* O(n * m)

## Rules

O notation describes how the amount of operations/memory needed by the algorithm grows as the arguments tend to infinity. This means that coefficients/constants are ignored. For example, O(100n) is the same as O(n).

# Time Complexity

Time complexity is the amount of time an algorithm takes to run relatiove to its input size. Usually more emphasized than space compexity.

## Examples

```
for (int num: arr) {
    print(num)
}
```

This algorithm has a time complexity of O(n). In the first for loop, a print operation is executed which is O(1). Since this is a loop iterating n times, the time complexity is O(1 * n) = O(n)

```
for (int num: arr) {
    print(num)}

for (int num: arr) {
    print(num)}

for (int num: arr2) {
    print(num)}}
```

This algorithm has a time complexity of O(n + m). The first two loops both print the same array, which is O(n). The third loop costs O(m), so together its O(n + m).

# Space Complexity 

Space complexity is the amount of memory allocated by the algorithm when run relative to the input size. For every variable initialized, memory is being allocated by the process. 

* Normally in interviews do not count the space compelxity of the input/output

## Examples

```
for (int num: arr) {
    print(num)
}
```
Since there is only one variable `num`, the space complexity is O(1).

```
Array nums = int[]
int oneHundredth = n / 100

for (int i = 0; i < oneHundredth; i++) {
    nums.add(arr[i])
}
```
This algorithm has a space complexity of O(n). The array nums stores the first 1% of numbers in arr. This gives a space complexity of O(n/100) = O(n).

*** UNDERSTAND THIS BETTER ***