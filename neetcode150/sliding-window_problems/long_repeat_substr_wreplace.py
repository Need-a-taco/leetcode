'''
My initial idea was solid, just trying to put the idea together,
just got a little lost in the sauce. I'll explain the implementation
in the second solution since this was better fleshed out. 
'''

def fst_sol(s: str, k: int) -> int:
    hmap = {}
    longest = max_freq = L = 0

    for R in range(len(s)):
        window_len = R - L + 1
        while (window_len) - max_freq > k:
            hmap[s[L]] -= 1
            L += 1
        if s[R] not in hmap:
            hmap[s[R]] = 1
        else:
            hmap[s[R]] += 1
            if hmap[s[R]].value() > max_freq:
                max_freq = hmap[s[R]].value()
    return longest

'''
IMPLEMENTATION: 
This is a sliding window problem, with a catepillar
inch-worm 
method

'''

def snd_sol(s: str, k: int) -> int:
    # Frequency map
    fmap = {}
    longest = L = R = 0
    
    while (R < len(s)):
        winlen = R - L + 1
        winmax = max(fmap.values())
        
        # Update the fmap
        if (s[R] not in fmap):
            fmap[s[R]] = 1
        else:
            fmap[s[R]] += 1
            
                
        # Move pointer L forward if needed
        while (winlen - winmax > k):
            fmap[s[L]] -= 1
            L += 1
            
            # Need to recalculate these variables
            winlen = R - L + 1
            winmax = max(fmap.values())
        
        if winlen > longest:
            longest = winlen
        R += 1
    return longest

# ChatGPT solution after being feed my snd_sol. 
def snd_gpt_sol(s: str, k: int) -> int:
    # Frequency map
    fmap = {}
    longest = L = R = 0
    
    while R < len(s):
        # Update the fmap
        if s[R] not in fmap:
            fmap[s[R]] = 1
        else:
            fmap[s[R]] += 1
        
        winmax = max(fmap.values())
        winlen = R - L + 1
        
        # Move pointer L forward if needed
        while winlen - winmax > k:
            fmap[s[L]] -= 1
            L += 1
            winlen = R - L + 1
            winmax = max(fmap.values())
        
        if winlen > longest:
            longest = winlen
        
        R += 1
    
    return longest


s1 = "ABAA"
k1 = 0
snd_sol(s1, k1)
        
