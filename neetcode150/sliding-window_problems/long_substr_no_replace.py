def lengthOfLongestSubstring(s: str) -> int:
    largest = 1
    hmap = {}
    same = False
    n = len(s)

    # This is not bad, but not completely right.
    for i in range(n):
        if (s[i] not in hmap):
            hmap[s[i]] = i
        else:
            x = i - hmap[s[i]]
            hmap[s[i]] = i
            if same == False:
                same = True
            if (x > largest):
                largest = x
    if not same:
        largest = n

    return largest

def snd_sol(s: str) -> int:
    # inch worm sliding window
    largest = 1
    setmap = set()
    L = 0
    if not s:
        return 0
    for i in range(len(s)):
        while setmap.intersection(s[i]) != set():
            setmap.remove(s[L])
            L += 1
        setmap.update({s[i]})
        if len(setmap) > largest:
            largest = len(setmap)
    return largest
            
# Neetcode essentially does the same thing,
# just slightly differently, which is a good sign

# However, for some reason this one is so much
# faster than mine. 
def neet_sol(s: str) -> int:
    setmap = set()
    L = largest = 0
    
    for i in range(len(s)):
        while s[i] in setmap:
            setmap.remove(s[l])
            L += 1
        setmap.add(s[i])
        # size of set works no?
        largest = max(largest, i - L + 1)
    return largest
test_str = "caab"
print(snd_sol(test_str))