'''
Given a string, find the length of the longest substring without repeating 
characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a 
substring.
'''

def longestSubstringWithoutDuplicate(s: str) -> int:
    NO_OF_CHAR = 256
    n = len(s)
    curr_max = 1
    max_so_far = 1
    visited = [-1] * NO_OF_CHAR

    visited[ord(s[0])] = 0

    for i in range(1, n):
        prev_index = visited[ord(s[i])]

        # If the currentt character is not present in the already 
        # processed substring or it is not part of the current NRCS, 
        # then do cur_len++ 
        if prev_index == -1 or (curr_max < i - prev_index):
            curr_max += 1
            
        # If the current character is present in currently considered 
        # NRCS, then update NRCS to start from the next character of 
        # previous instance. 
        else:
            if curr_max > max_so_far:
                max_so_far = curr_max

            curr_max = i - prev_index

        visited[ord(s[i])] = i
    return max_so_far 

print(longestSubstringWithoutDuplicate('pwwkew'))