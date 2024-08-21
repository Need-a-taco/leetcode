'''
My initial solution was to have a inch worm sliding window 
and maintaining a set so that we could compare permutations of
the window and permutations of s1. However, this ran into 
issues of duplicate letters, because when I would remove a
character from a set, however, there is should still be one
in our window. I tried then to use a frequency hashmap as
we iterated, and only remove the element from the set if the
frequency map reached zero for a certain letter. Perhaps this
is a viable solution, I don't see why not. However, in my
implementation, I got a bit bogged down in errors. "
'''

def fst_sol(s1: str, s2: str) -> bool:
    # window size
    w = len(s1)
    L, R = 0, w - 1

    set_check = {s1[0]}
    set_map = {s2[0]}
    freq_map = {}
    
    for i in range(1, len(s1)):
        set_check.update({s1[i]})
    for i in range(1, len(s1)):
        set_map.update({s2[i]})
    for i in range(len(s1)):
        if s1[i] not in freq_map:
            freq_map[s2[i]] = 1
        else:
            freq_map[s2[i]] += 1
    print(set_map, freq_map)

    while (L <= len(s2) - len(s1)):
        print(set_map)
        print(freq_map)
        if set_map == set_check:
            return True
        if R == len(s2) - 1:
            break

        # first, let's deal with the right pointer...
        if s2[R + 1] not in set_map:
            set_map.update({s2[R + 1]})
            freq_map[s2[R + 1]] = 1
        elif s2[R + 1] in set_map:
            freq_map[s2[R + 1]] += 1
        R += 1 

        # now left pointer
        if freq_map[s2[L]] <= 1:
            set_map.remove(s2[L])
            freq_map[s2[L]] -= 1
        elif freq_map[s2[L]] > 1:
            freq_map[s2[L]] -= 1
        L += 1
    return False

s1 = "adc"
s2 = "dcda"

'''
However, it is not the best way. The best way is to use two
hashmaps, one for s1 and one for s2. However, we do not
want to simply compare hashmaps, as that adds a lot of extra
arithmetic operations and comparisons to do. Instead, we will
use a variable called matches.

We should have 26 matches if we detect a permutation match. This
means that the count for each of the letters in our sliding
window of s2 matches the counts for all of the letters in s1.
'''

def snd_sol(s1: str, s2: str) -> bool: 
    # Setting up our hashmaps to keep track of character counts
    s1_map = {}
    s2_map = {}
    
    for i in range(97, 123):
        s1_map[chr(i)] = 0
        s2_map[chr(i)] = 0
    
    for c in s1:
        s1_map[c] += 1
    
    for c in s2[0:len(s1)]:
        s2_map[c] += 1
        
    # Initialize and find our matches var
    matches = 0
    for i in range(97, 123):
        if (s1_map[chr(i)] == s2_map[chr(i)]):
            matches += 1
    
    # Try a two pointers way of iterating through s2
    L, R = 0, len(s1) - 1
    while (R < len(s2) - 1):
        if matches == 26:
            print(True)
        
        L_was_match = True if (s1_map[s2[L]] == s2_map[s2[L]]) else False
        R_was_match = True if (s1_map[s2[R]] == s2_map[s2[R]]) else False
        
        # If no match, increment the window by 1
        # and update the s2 char-count map
        s2_map[s2[L]] -= 1
        L += 1
        R += 1
        s2_map[s2[R]] += 1
        
        # Update matches variable
        if L_was_match and (s1_map[s2[L]] != s2_map[s2[L]]):
            matches -= 1
        elif (not L_was_match) and (s1_map[s2[L]] == s2_map[s2[L]]):
            matches += 1
        if R_was_match and (s1_map[s2[R]] != s2_map[s2[R]]):
            matches -= 1
        elif (not R_was_match) and (s1_map[s2[R]] == s2_map[s2[R]]):
            matches += 1
            
    return (matches == 26)

def snd_sol(s1: str, s2: str) -> bool: 
    # Setting up our hashmaps to keep track of character counts
    s1_map = {chr(i): 0 for i in range(97, 123)}
    s2_map = {chr(i): 0 for i in range(97, 123)}
    
    for c in s1:
        s1_map[c] += 1
    
    for c in s2[0:len(s1)]:
        s2_map[c] += 1
        
    # Initialize and find our matches var
    matches = 0
    for i in range(97, 123):
        if s1_map[chr(i)] == s2_map[chr(i)]:
            matches += 1
    
    # Try a two-pointers way of iterating through s2
    L, R = 0, len(s1) - 1
    while R < len(s2) - 1:
        if matches == 26:
            return True
        
        R += 1
        s2_map[s2[R]] += 1
        
        if s1_map[s2[R]] == s2_map[s2[R]]:
            matches += 1
        elif s1_map[s2[R]] + 1 == s2_map[s2[R]]:
            matches -= 1
        
        if s1_map[s2[L]] == s2_map[s2[L]]:
            matches -= 1
        elif s1_map[s2[L]] == s2_map[s2[L]] + 1:
            matches += 1
        
        s2_map[s2[L]] -= 1
        L += 1
    
    return matches == 26

s1 = "ab"
s2 = "eidbaooo"

# Gonna give it a third try after getting 