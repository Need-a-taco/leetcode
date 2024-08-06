def fst_sol(nums: list[int]) -> list[int]:
    # This is a brute force solution. O(n^2) time. 
        n = len(nums)
        output = []

        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod = prod * nums[j]
            output.append(prod)
        return output

nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]

def snd_sol(nums: list[int]) -> list[int]:
    # Kind of fast. It memoizes two 1D tables
    n = len(nums)
    output = []
    prefix = []
    postfix = []

    front_prod = 1
    back_prod = 1
    for i in range(n):
        front_prod *= nums[i]
        back_prod *= nums[n - i - 1]
        prefix.append(front_prod)
        postfix.append(back_prod)
    postfix.reverse()
      
    for i in range(n):
        if i == 0:
            output.append(postfix[i + 1])
        elif i == (n - 1):
            output.append(prefix[n - 2])
        else:
            prod = prefix[i - 1] * postfix[i + 1]
            output.append(prod)
    return output

def neet_sol(nums: list[int]) -> list[int]:
    # This one is incredibly fast, and doesn't 
    # require as much memoization
    n = len(nums)
    output = [1] * n
    
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
        
    postfix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]
        
    return output
print(neet_sol(nums2))