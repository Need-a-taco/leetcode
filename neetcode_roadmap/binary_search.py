# Hey let's go, it works!   
def fst_sol(nums: list[int], target: int) -> int:
    L, R = 0, len(nums) - 1
    M = (L + R) // 2
    while (nums[M] != target) and (L < R):
        print(f"L:{L}, R: {R}, M: {M}")
        if nums[M] < target:
            L = M + 1
        if nums[M] > target:
            R = M - 1
        M = (L + R) // 2
    if nums[M] == target:
        return M
    return -1
print(fst_sol([-1,0,3,5,9,12], 9))