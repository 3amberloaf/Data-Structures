# Recuurence Relation Induction

In recurrence relations, the function f(n) is referred to as T(n).

## T(n) = T(n-1) + 1
```c
void Test(int n)
{
    if (n> 0)
    {
        printf("/d", n); // --> takes 1 Unit of Time
        Test(n-1); // --> Takes T(n -1) unit of time
    }
}
Test(3)
```

In this function, we first call Test on the number 3 which takes one time unit. Then it decreases the number to 2 and repeats until it reaches 0 and stops. It takes 3 units of time to print the value, but there are four calls which is 4 units. Therefore, if we pass the value `n`, it will print `n` times but make `n + 1` calls. 

### Total Time

To find the total time, you add the time units. We ignore the conditions when adding time units because only need 1 as a constant.

T(n) = { 1          n = 0 }
        T(n-1) + 1  n > 0

### Substitution Method

We want to solve for T(n -1).
1. T(n) = T(n-1) + 1
- Since we know that T(n) = T(n-1) + 1, then we can substitute this into T(n-1) + 1
2. T(n-1) = T(n -2)+ 1
3. Now we substitute T(n-1) back into the original
- T(n) = [T(n-2) + 1] +1
- T(n) = T(n-2) + 2
4. Substitute one more time
- T(n) = T(n-3) + 3
5. Continue k times
- T(n) = T(n - k) + k
