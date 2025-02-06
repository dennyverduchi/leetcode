# Q1. Maximum Difference Between Even and Odd Frequency I
# Easy
# 3 pt.

# You are given a string s consisting of lowercase English letters. Your task is to find the maximum difference between the frequency of two characters in the string such that:
# One of the characters has an even frequency in the string.
# The other character has an odd frequency in the string.
# Return the maximum difference, calculated as the frequency of the character with an odd frequency minus the frequency of the character with an even frequency.

# Example 1:
# Input: s = "aaaaabbc"
# Output: 3
# Explanation:
# The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
# The maximum difference is 5 - 2 = 3.

# Example 2:
# Input: s = "abcabcab"
# Output: 1
# Explanation:
# The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
# The maximum difference is 3 - 2 = 1.

class Solution:
    def maxDifference(self, s: str) -> int:
        count = [s.count("a"), s.count("b"), s.count("c"), s.count("d"), s.count("e"), s.count("f"), s.count("g"), s.count("h"), s.count("i"), 
                 s.count("j"), s.count("k"), s.count("l"), s.count("m"), s.count("n"), s.count("o"), s.count("p"), s.count("q"), s.count("r"), 
                 s.count("s"), s.count("t"), s.count("u"), s.count("v"), s.count("w"), s.count("x"), s.count("y"), s.count("z")]
        count.sort(reverse=True)
        odd = [0] * len(count)
        even = [0] * len(count)
        for i in range(len(count)):
            if count[i] % 2 != 0:
                odd[i] = count[i]
            else:
                even[i] = count[i]
        return max(odd) - (min(filter(lambda x: x > 0, even)))