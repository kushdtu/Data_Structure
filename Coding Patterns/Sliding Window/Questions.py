import sys

'''
Given a string s that consists of only uppercase English letters,
you can perform at most k operations on that string. In one operation,
you can choose any character of the string and change it to any other uppercase
English character.

Find the length of the longest sub-string containing all repeating letters
you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:
Input:
s = "ABAB", k = 2
Output: 4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input:
s = "AABABBA", k = 1
Output:4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

def characterReplacement(s, k):
    n = len(s)
    if n == 0:
        return 0
    def findLen(s, k, ch):
        l, r = 0, 0
        max_len = 1
        count = 0

        while r < n:

            if s[r] != ch:
                count += 1
            
            while count > k:
                if s[l] != ch:
                    count -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len

    max_len = 1
    for i in range(26):
        max_len = max(max_len, findLen(s, k, chr(i + ord('A'))))

    return max_len 

# print(characterReplacement('HHHHHH', 4))

'''
Given a string s and a non-empty string p, find all the start indices of p's 
anagrams in s.
Strings consists of lowercase English letters only and the length of both 
strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output: [0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output: [0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
MAX = 256
def findAnagramUtil(countP, countSW):
    for i in range(MAX):
        if countP[i] != countSW[i]:
            return False
    return True

def findAnagram(pat, txt):
    M = len(pat)
    N = len(txt)
    
    countP = [0]*MAX
    countTW = [0]*MAX
    result = []
    for i in range(M):
        (countP[ ord(pat[i]) ]) += 1
        (countTW[ ord(txt[i]) ]) += 1

    for i in range(M, N):

        if findAnagramUtil(countP, countTW):
            result.append(i-M)

        (countTW[ ord(txt[i]) ]) += 1
        (countTW[ ord(txt[i-M]) ]) -= 1

    if findAnagramUtil(countP, countTW):
        result.append(N-M)
    return result

txt = "BAA"
pat = "AA"  
# print(findAnagram(pat, txt))


'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
'''

def checkInclusion(pat, txt):
    M = len(pat)
    N = len(txt)
    
    countP = [0]*MAX
    countTW = [0]*MAX

    for i in range(M):
        (countP[ ord(pat[i]) ]) += 1
        (countTW[ ord(txt[i]) ]) += 1

    for i in range(M, N):

        if findAnagramUtil(countP, countTW):
            return True

        (countTW[ ord(txt[i]) ]) += 1
        (countTW[ ord(txt[i-M]) ]) -= 1

    if findAnagramUtil(countP, countTW):
        return True
    return False

pat = "ab"
txt = "eidbaooo"
# print(checkInclusion(pat, txt))

'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
'''

def longestOnes(A: [int], K: int) -> int:
    n = len(A)
    start = 0
    count = 0
    max_ones = 0
    curr_max_ones = 0

    for i in range(n):

        if A[i] == 0:
            count += 1

        curr_max_ones += 1
        while count > K:
            if A[start] == 0:
                count -= 1
            start += 1
            curr_max_ones = i - start + 1
        
        if curr_max_ones >= max_ones:
            max_ones = curr_max_ones

    return max_ones

A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
# print(longestOnes(A, K))

d  = dict()
d[1,1] = 5
d[1,2] = 6
print(d)
    