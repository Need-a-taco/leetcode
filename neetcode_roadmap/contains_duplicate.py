def fst_sol(self, nums: list[int]) -> bool:
        prevMap = {} # Keep track of if we've seen it before. 
        for num in nums:
            if num in prevMap:
                return True
            else:
                prevMap[num] = 1
        return False