'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

def minWindow(S: str, T: str) -> str:
    if not S or not T:
        return ""
    
    hash_t = dict()
    for letter in T:
        hash_t[letter] = hash_t.get(letter, 0) + 1

    required = len(hash_t)
    l, r = 0, 0
    ans = (float("inf"), None, None)
    current_window_hash = dict()
    formed = 0

    while r < len(S):
        character = S[r]
        current_window_hash[character] = current_window_hash.get(character, 0) + 1

        if character in hash_t and current_window_hash[character] == hash_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = S[l]
            if r - l + 1 < ans[0]:
                ans = (r-l+1, l, r)

            current_window_hash[character] -= 1
            if character in hash_t and current_window_hash[character] < hash_t[character]:
                formed -= 1

            l += 1
        r += 1 

    return "" if ans[0] == float("inf") else S[ans[1]: ans[2] + 1]

S = "ADOBECODEBANC"
T = "ABC"
print(minWindow(S, T))