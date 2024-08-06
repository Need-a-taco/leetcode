# Brute force implementation. Works, but timed out,
# passed 198/212 test cases, meaning it works but
# fails on the tests that really test efficiency. 

# Cool that this implentation was so easy to code I guess.
def fst_sol(prices: list[int]) -> int:
        n = len(prices)
        largest_profit = 0
        for i in range(n - 1):
            for j in range(i, n):
                profit = prices[j] - prices[i]
                if (profit > largest_profit):
                    largest_profit = profit
        return largest_profit
    
# Now to figure out the trick for O(n). 
# Check scrap paper notes
def snd_sol(prices: list[int]) -> int:
        n = len(prices)
        L = prices[0]
        largest = 0
        for i in range(1, n):
            R = prices[i]
            if (R - L > largest):
                largest = R - L
            if (R < L):
                L = R
        return largest