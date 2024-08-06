k = 2
nums = [1,1,1,2,2,3]

def fst_sol(nums: list[int], k: int) -> list[int]:
    hmap = {}
    output = []

    for num in nums:
        if num in hmap:
            hmap[num] += 1
        else:
            hmap[num] = 1

    for _ in range(k):
        largest = [0, 0]
        for num in hmap.keys():
            if hmap[num] > largest[1]:
                largest[0], largest[1] = num, hmap[num]
            output.append(largest[0])
            hmap.pop(largest[0])
    return output

# Runs into RuntimeError, which is new to me. Basically,
# it seems like we are not allowed to change size of
# a dictionary like it's a mutable data structure. 

# Bucket Sort hashmap implementation
def snd_sol(nums: list[int], k: int) -> list[int]:
    hmap = {}
    freq = [[] for _ in range((len(nums) + 1))]
    
    # Alt way to add kv pairs of ints and freqs
    for num in nums:
        hmap[num] = 1 + hmap.get(num, 0)
    for num, count in hmap.items():
        freq[count].append(num)
    
    output = []
    for i in range(len(freq) - 1, 0, -1):
        for j in freq[i]:
            output.append(j)
            k -= 1
            if k == 0:
                return output