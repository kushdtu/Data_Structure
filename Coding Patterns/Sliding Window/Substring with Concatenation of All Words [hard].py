from typing import List

'''
Substring with Concatenation of All Words.
You are given a string, s, and a list of words, words, that are all of the same 
length. Find all starting indices of substring(s) in s that is a concatenation of 
each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''

def findSubstring(s: str, words: List[str]) -> List[int]:
    if len(s) == 0 or len(words) == 0:
        return []
    n = len(s)
    wordsCount = len(words)
    wordSize = len(words[0])
    wordsLen = wordsCount * wordSize
    if n < wordsLen:
        return []
    hashMap = dict()
    res = []
    
    for word in words:
        if word in hashMap:
            hashMap[word] += 1
        else:
            hashMap[word] = 1
    
    for i in range(0, n - wordsLen + 1):
        count = wordsCount
        tempHash = hashMap.copy()
        j = i
        while j < i + wordsLen:
            word = s[j:j+wordSize]
            if word not in tempHash or tempHash[word] == 0:
                break
            else:
                count -= 1
                tempHash[word] -= 1
            j += wordSize
        if count == 0:
            res.append(i)
    return res

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(findSubstring(s, words))
    