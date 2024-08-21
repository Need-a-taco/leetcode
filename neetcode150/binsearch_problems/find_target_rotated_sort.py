'''
This is to account for all the possible cases. We want to narrow
down the binary search to a portion of the list that is not
rotated, meaning for all indices from L to R, it holds that
L < L + 1 < ... < R - 1 < R. 

On top of that, the sorted portion has to contain the target
value, which should be possible to narrow down, since portions
of the array still are sorted, so we can compare endpoints to
eliminate subportions of the array that we know do not have the
target value. 

Thus, we have to be able to make conclusions about where this
portion with the target is.

So right off the bat, given some indices L and R, if 
nums[L] < nums[R], then we know that that subarray is completely
sorted. However, if nums[L] < nums[R], it means there is some
rotation somewhere in the subarray. So if the conditional test
nums[L] < nums[R] does not pass, then we should use testing with
the binary slice, calculating M = (L + R) // 2, in order to
eliminate part of the array. 

So after we find this new M var, suppose the subarray from L to
R is rotated sort. Assume up to this point, the target is in
here. Let's see these two cases to narrow down the subarray. 

'''

def fst_sol(nums: list[int], target: int) -> int:
    L, R = 0, len(nums) - 1
    
    # Regular binary search
    if (nums[L] < nums[R]):
        M = (L + R) // 2
        while (nums[M] != target) and (L < R):
            if nums[M] < target:
                L = M + 1
            if nums[M] > target:
                R = M - 1
            if nums[M] == target:
                return M
        return -1
    
    M = (L + R) // 2
    if nums[M] == target:
        return M
    if (nums[M] < nums[R] < nums[L]):
        if (nums[M] < target < nums[R]):
            L = M + 1
        else:
            R = M - 1
    elif (nums[R] < nums[L] < nums[M]):
        if (nums[L] < target < nums[M]):
            R = M - 1
        else:
            L = M + 1
# This is getting stupid. 

'''
Before, I was thinking of too many different cases, I was thinking
of narrowing it down to a very specific subarray. This is still good,
but instead we should think about if we are in the left-sorted part
of the array or the right part of the sorted array. Note that if the
array is not rotated sorted, then there is no such distinction.

The line <if (M == target):> is just to catch if we have already
arrived at the right index.  However, the two conditionals below
that are to check if M is in the left or right sorted portion. 

Logically, if nums[L] < nums[M], then that means that the "drop"
has not happened between L and M, which means that M is still in
the left sorted portion. It is possible that the whole thing is
sorted too. 

If not nums[L] < nums[M], that means that the drop has happened
somewhere between L and M, and so M is in the right sorted portion.
So we have these two conditionals to find if we are in the left or
right sorted portion. From there, we will do different things in
each of these cases.

In the case where nums[L] < nums[M], we want to know if the target
is in this interval. So we know M is in the left sorted portion.
What we are essentially going to do is test if we should stay in
this interval of (nums[L], nums[M]), which we know is sorted. 

The way we will test if the target is out of the interval is to see
if the target is greater than nums[M] or less than nums[L]. In
either of those cases we wanna push our binsearch window to the left, 
and move our left pointer to the right. 

If the target is in the interval, then we should shrink our search
by moving the right pointer left so that we are binary searching and
just looking in this left-sorted subarray. 
'''

def snd_sol(nums: list[int], target: int) -> int:
    L, R = 0, len(nums) - 1
    
    while (L <= R):
        M = (L + R) // 2
        if (target == nums[M]):
            return M
        if nums[L] <= nums[M]:
            if target > nums[M] or target < nums[L]:
                L = M + 1
            else:
                R = M - 1
        else:
            if target < nums[M] or target > nums[R]:
                R = M - 1
            else:
                L = M + 1
    return -1
        
    
print(snd_sol([3,5,6,0,1,2], 5))
    
     
    