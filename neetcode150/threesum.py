# Doesn't quite work
def fst_sol(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    complements = {}
    output = []
    for i in range(n):
        complement = -1 * nums[i]
        if complement not in complements:
            complements[complement] = [i]
        else:
            complements[complement].append(i)
    for i in range(n - 1):
        for j in range(i + 1, n):
            complement = -1 * (nums[i] + nums[j])
            matches = complements[complement]
            print(matches)
            if (max(matches) > j):
                new_lst = sorted([nums[i], nums[j], complement])
                if new_lst not in output:
                    output.append(new_lst)         
    return output
