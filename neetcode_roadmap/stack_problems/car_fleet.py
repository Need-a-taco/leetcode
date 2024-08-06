# Right off the bat, just reading the premise of the problem
# I think this is one of the most fun ones I have done. It's
# such a funny sounding question and it leaves me wanting to
# know how to solve it. 

# I can think of a very inefficient solution without using a stack.
# Basically think of it like parameterizing each of the positions
# of the cars at each hour. 
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # sort the cars by their starting position
        for p, s in sorted(cars)[::-1]: # reverse sorted order
            time = (target - p) / s
            if not stack:
                stack.append(time)
            else:
                prevTime = stack[-1]
                if time > prevTime:
                    stack.append(time)
        
        return len(stack)
    
    
def neet_sol(target: int, position: list[int], speed: list[int]) -> int:
    cars = [[p, s] for p, s in zip(position, speed)]
    stack = []

    # sort the cars by their starting position
    for p, s in sorted(cars)[::-1]: # reverse sorted order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
