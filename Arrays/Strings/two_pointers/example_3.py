# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# go through each index in s and see if its in t, if it is then return True


class Solution:
    def check_subsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                # if the letters match then go to the next letter in s
                i += 1
            # despite if the letters match we still need to go through the rest of j
            j += 1
        
        return i == len(s)