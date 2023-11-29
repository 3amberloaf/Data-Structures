# Given a string s, return true if it is a palindrome, false otherwise.

def palidrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# left is going from left to right
# right is going from right to left
# the while loop sets up the function and the function compares the letters by looking at their indices

