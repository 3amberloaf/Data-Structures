# Big O

Big O notation described the computational complexity of an algorithm via:

    - time complexity
    - space complexity

N is the input size. The statement f(n) is g(n) means that the growth rate of f(n) is no more than the growth rate of g(n)

## Examples

* O(n)
* O(n^2)
* O(2^n)
* O(log n)
* O(n * m)

## Rules

O notation describes how the amount of operations/memory needed by the algorithm grows as the arguments tend to infinity. This means that coefficients/constants are ignored. For example, O(100n) is the same as O(n). 

### Big Omega

f(n) is Ω(g(n)) if there is a constant c > 0 and an integer constant n0 ≥ 1 such that f(n) ≥ c g(n) for n ≥ n0
**f(n) is greater than or equal to g(n)**

### Big Theta

f(n) is Θ(g(n)) if there are constants c’ > 0 and c’’> 0 and an integer constant n0 ≥ 1 such that c’g(n) ≤ f(n) ≤ c’’g(n) for n ≥ n. A function is big theta if its big omega and big oh.
**f(n) is equal to g(n)**

# Time Complexity

Time complexity is the amount of time an algorithm takes to run relatiove to its input size. Usually more emphasized than space compexity.

## Examples

```python
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

### Functions

To formally show that these equations are O(n) or not, find a constant c and value n0 that the equality is <= cn and n >= n0.

1. n^2 is not O(n)

It is not O(n) because for n^2 to be O(n), there would need to be a constant multiplied by n to make it larger than n^2. This gives us n^2 <= cn which can be reduced to n <= c . This statement is impossible because c is a constant, and no matter how big it is n can always be greater. This shows us that n^2 grows faster than O(n). 

2. 7n - 2

Let c = 7 and n0 = 1

7n-2 <= cn for all n >= n0
7n-2 <= 7n for all n >= 1

This inequality is O(n) because 7n-2 <= 7n when n is positive. 

3. 3n^3 + 20n^2 + 5

Let c = 4 and n0 = 21

3n^3 + 20n^2 + 5 <= cn^3 for all n >= n0
3n^3 + 20n^2 + 5 <= 4n^3 for all n >= 21

This equation is not O(n) but is actually O(n^3).

4. 3logn + 5

let c = 8 and n0 = 2

3logn + 5 <= c log n for all n >= n0
3logn + 5 <= 8 log n for all n>= 2

This equation is O(logn)

5. 5n^2 

let c = 5 and n0 = 1

5n^2 >= 5(n^2) for all n >= 1 // Ω(n^2)
5n^2 <= 5n^2 for all n>= 1 // O(n^2)
5n^2 <= 5n^2 for all n>= 1 // Θ(n^2)