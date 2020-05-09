from typing import List
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
class Solution:
    def findAnagramsUtil(self, countP, countCurrentWindow):
        for i in range(256):
            if countP[i] != countCurrentWindow[i]:
                return False
        return True
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        M = len(p)
        N= len(s)
        countP = [0]*256
        countCurrentWindow = [0]*256
        res = []
        
        if M > N:
            return []
        
        for i in range(M):
            countP[ord(p[i])] += 1
            countCurrentWindow[ord(s[i])] += 1
        
        for i in range(M, N):
            if self.findAnagramsUtil(countP, countCurrentWindow):
                res.append(i-M)
            
            countCurrentWindow[ord(s[i])] += 1
            countCurrentWindow[ord(s[i-M])] -= 1
        
        if self.findAnagramsUtil(countP, countCurrentWindow):
            res.append(N-M)
        
        return res
                