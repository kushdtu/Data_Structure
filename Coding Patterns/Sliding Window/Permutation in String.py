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

class Solution:
    def findAnagramsUtil(self, countP, countCurrentWindow):
        for i in range(256):
            if countP[i] != countCurrentWindow[i]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = s2
        p = s1
        if not s or not p:
            return []
        M = len(p)
        N= len(s)
        countP = [0]*256
        countCurrentWindow = [0]*256
        
        if M > N:
            return []
        
        for i in range(M):
            countP[ord(p[i])] += 1
            countCurrentWindow[ord(s[i])] += 1
        
        for i in range(M, N):
            if self.findAnagramsUtil(countP, countCurrentWindow):
                return True
            
            countCurrentWindow[ord(s[i])] += 1
            countCurrentWindow[ord(s[i-M])] -= 1
        
        if self.findAnagramsUtil(countP, countCurrentWindow):
            return True
        
        return False