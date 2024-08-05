''' 
This works, and it's pretty fast, beat's ~90% of users. This basically uses
a hashmap, where the keys are the letters and the values are the frequencies
of the how many times the letter showed up in the word. The second time
around, we simply check if those same letters are in the hashmap. If it is,
we decrement the values of the key hashed into. We only return False in this
second for loop if there is a letter which is not in the hashmap at all, at
which point we know it is not an anagram.

Then, we have to check if the letters that we do share have the same counts.
That means that incrementing and decrementing should bring all the counts
to zero, so we check if all the values in our hashmap are 0. 
'''
def fst_sol(self, s: str, t: str) -> bool:
    prevMap = {}

    # Set up hashmap from og str
    for letter in s:
        if letter in prevMap:
            prevMap[letter] += 1
        else:
            prevMap[letter] = 1

    # Verify with second str
    for letter in t:
        if letter in prevMap:
            prevMap[letter] -= 1
        else:
            return False

    for value in prevMap.values():
        if (value != 0):
            return False
    return True