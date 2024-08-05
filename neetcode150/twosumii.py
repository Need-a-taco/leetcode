def fst_sol(numbers: list[int], target: int) -> list[int]:
    L, R = 0, -1
    while numbers[L] + numbers[R] != target:
        sum = numbers[L] + numbers[R]
        if sum < target:
            L += 1
        else:
            R -= 1

    return [L + 1, len(numbers) + R + 1]