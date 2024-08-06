def fst_sol(nums: list[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            M = (L + R) // 2
            print(f"L: {L}, M: {M}, R: {R}")
            left_min = min(nums[L], nums[M])
            right_min = min(nums[M], nums[R])
            print(f"left_min: {left_min}, right_min: {right_min}")
            if (left_min < right_min):
                R = M - 1
            elif (right_min < left_min):
                L = M + 1
            else:   # meaning right_min == left_min
                print(f"returning: {nums[M]}")
                return nums[M]
        print(f"returning: {nums[L]}")
        return nums[L]

# Welp, this passes 124/150 tests, but I feel like at this point
# I'm just trying to game the unit tests and I'm not on track
# to the most succint solution. 
def snd_sol(nums: list[int]) -> int:
    L, R = 0, len(nums) - 1
    while (L < R) and (R - L > 3):
        M = (L + R) // 2
        mini = min(nums[L], nums[M], nums[R])
        if (nums[R] == mini):
            L = M + 1
        else:
            R = M - 1
    if (R - L <= 3):
        print(min(nums[L : R + 1]) )
        return min(nums[L : R + 1]) 
    print(nums[L])
    return nums[L]
        
def neet_sol(nums: list[int]) -> int:
    res = nums[0]
    L, R = 0, len(nums) - 1
    while (L <= R):
        if (nums[L] < nums[R]):
            res = min(res, nums[L])
            break
        
        M = (L + R) // 2
        res = min(res, nums[M])
        if nums[M] >=  nums[L]:
            L = M + 1
        else:
            R = M - 1
        return res  
snd_sol([4,5,1,2,3])
