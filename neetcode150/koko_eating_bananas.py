# This had me so confused. I think the lesson learned is that unless it is completely
# necessary, stay awake from while loops. 
def fst_sol(piles: list[int], h: int) -> int:
    n = len(piles)
    possible_values = list(range(n, max(piles) + 1))
    print(possible_values)
    L, R = 0, len(piles) - 1
    print(L, R)
    
    while L <= R:
        # Vars needed for greedy algo test
        copy, hours = possible_values, h
        M = (L + R) // 2
        bananas = possible_values[M]
        # Test if the middle index works
        while (max(copy) > 0) and (h > 0):
            copy[copy.index(max(copy))] -= bananas
            hours -= 1
        if (max(copy) > 0) and (hours <= 0):
            L = M + 1
        else:
            R = M - 1
        print(L, R)
    print(possible_values[L])

piles = [30,11,23,4,20]
h = 5

    