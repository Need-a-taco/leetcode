''' Notes for understanding
###################################################
# There's a lot syntactically to figure out

closeToOpen = { ')' : '(',
                ']' : '[',
                '}' : '{' }

print(')' in closeToOpen) # Prints True
# This really checks if the string ")" is in the dictionary keys 

# Let's just practice using a stack a little bit. In Python, 
# we can just use an array with the append and pop list methods.

lst = []
lst.append("0")
print(lst)
lst.append("1")
print(lst)
lst.pop()
print(lst)

# The code above prints the following: 
['0']
['0', '1']
['0']

# Another useful trick to know is indexing with neg.
# nums. 

lst = [0, 1, 2]
print(lst[-1])
print(lst[-2])
print(lst[-3]) # This prints the following 

2
1
0

# So basically, 0 is the first element in the list. If
# we increment 0, it goes one by one to the left. If we have
# index -1, we jump all the way to the right side of the list,
# and with each decrement we go one to the left. 

# Another piece of syntax to understand is the when we include
a variable after keyword <if> without any sort of relation 
operator like <, >, =, etc. In this case, it checks if that variable
is empty. It works for lists, dictionaries, tuples, sets, or data
type that can have a length really.

lst = []
if lst:
    print(True)
else:
    print(False) # This prints False because the list is empty
    
# This can be shortened to the following one line syntax
print(True if lst else False) # Prints False as well


dict = {"a" : "b"} # For dictionaries
if dict:
    print(True) # Prints True
    
    
tup = (0, 1) #  For tuples
if tup:
    print(True) # Prints true
    
# Now, we should have all the pieces syntactically to understand
Neetcode's solution. 
'''

def neet_sol(s: str) -> bool:
    stack = []
    closeToOpen = { ')' : '(',
                    ']' : '[',
                    '}' : '{' }

    for c in s:
        if c in closeToOpen:
            if stack and (stack[-1] == closeToOpen[c]):
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

''' ################################################
# For any implementation, we need to make a clear distinction between
# the opener parentheses and the closers. For this one specifically,
# this is done by keeping all of the closers as the dict keys and 
# openers as the dict values. 

# Also, we know that the characters in the string will only ever
# be the ones outlined on Leetcode, so we don't have to worry about
# edge cases where the string has some random other chars.

# Basically, our implementation hinges on the following fact. If
# we see a closer, it either needs to be the closer for its
# corresponding opener, or all other parentheses must be closed, which
# means our stack would be empty. If the closer doesn't satisfy the
# first condition, it could be something invalid like "()}". If it
# doesn't satisfy the second, it could be something like "}". 

# Zooming out for a sec, our implementation iterates through all of
# the chars in the string and performs certain conditionals based
# on whether the char we are on is a opener or closer. We just went
# over the two conditionals to check. 

# If they are satisfied, that means that we have successfully closed 
# an unclosed parenthesis, which by the logic of a stack means we 
# should pop off the top element. If both are not satisfied, we
# instantly know we have a invalid parentheses. This is all done with
# the code:

if c in closeToOpen:
    if stack and (stack[-1] == closeToOpen[c]):
        stack.pop()
    else:
        return False
        
# In the code above, c is the variable name for each char. The top line
# is simplifies, but the Python syntax basically checks if the char is
# one of the keys, which we know is all of the closers. This, it returns
# a boolean for whether this char is a closer. True if closer, False if
# opener. If true, we run through the following two conditionals. 

# The second line runs for closers. It checks if the stack has stuff in
# it, because encountering a closer while the stack is empty instantly
# invalidates the string. Then, it checks if the -1 index, or rightmost
# of the list, or more abstractly the top of the stack, matches the
# corresponding opener of the char we are currently iterating on. 

# This check above is done with a dictionary search. If both of these
# are satisfied, the string is valid up until this point. We still need
# to address what to do if we encounter an opener. Assuming that the
# string is valid up to this point, encountering an opener doesn't
# invalidate the string. We just need to add this opener to the stack.

else:
    stack.append(c) # Use append method to add to the stack
    
# That is done with this code. Finally, if we've iterated through all
# the chars and haven't returned False yet, it means that we haven't found
# any opener-closer mismatches, since this is the only scenario in the
# code above where we would return False. However, we have not accounted
# for parentheses that were opened but never closed.

# If a parenthesis is closed, it is popped off the top of the stack. This,
# if it is unclosed, it should still be on the stack. Thus, we can simply
# check if the stack is empty. The string is valid if the stack has been
# emptied at the end, as this means no unclosed parentheses. It's invalid
# if there is still stuff in the string, which means something is unclosed.

return True if not stack else False

# This is done syntactically succintly with this one line of code above.
'''
