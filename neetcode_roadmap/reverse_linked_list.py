'''
First, a bit of a refresher on object-oriented programming and Linked Lists. 
This is how classes are implemented. 
###############################################################################


class Robot():
    def __init__(self, name : str, age=4):
        self.name = "robot " + name
        self.age = age
        self.age_next_year = age + 1
    def greet(bot : 'Robot'):
        print(f"Hi, my name is {bot.name}")

timmy = Robot("Timmy", 5)
print(timmy.age_next_year)
timmy.greet()


###############################################################################
When you define a class, you need the keyword <class> at the beginning, just
like you need <def> when you define a function. From there, the next layer of
indentation is where you define the functions. Every class at least needs a
function called <__init__> with a parameter called 'self', and for actual use
you'll probably include other variables too. 

Actually, I did some investigating and you can apparently do this as well...
This completely works, but idk why you would ever do this. 


class Robot():
    def __init__():
        1 + 1
bot1 = Robot


With all that being said, look at the class implementation of a Linked List
below. 
'''
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

'''
###############################################################################


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

node1.val = node1.val
print(node1.val)

current_node = node1
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next


###############################################################################
This prints 1 2 3 in the terminal. Now let's go over the Leetcode solution
conceptually for reversing a linked list. 
'''
from typing import Optional
def fst_sol(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

'''
Note that we import the "typing hint", Optional, from Python's typing 
module. When used for specifying typing in the function definition, it
indicates that arguments can either be of the specified type, or it
could also be of type None. 

Anyways, on to the reversing of a linked list implementation. The
concept of interating through the linked list and reversing the direction
of the pointer arrows is quite simple. However, the execution is new to me,
especially since I don't know how to iterate through a linked list. The
example above of printing the values in the LL is good for hinting at how
we can do this. 

We will start at the head of the LL. We are gonna use two "pointer"
variables that iterate through: prev, and curr. We should think like this
because the LL class already has the functionality of a next parameter
built in. Thus, we will reroute the arrows to point from curr to prev, which
really means set curr.next = prev at some point in the code.

If prev, curr start at the head, then prev = None. curr should be the first
node, and prev will be undefined. That makes sense as we are reversing it, so
the last node should point to undefined. Then, as promised, we will do 
<curr.next = prev>. In order to iterate through the list, we need to increment
curr to the next node with the next functionality, like <curr = curr.next>.

However, curr.next has already been updated to prev. Thus, we have our temp
variable, called nxt, to store the value of the next pointer. Thus, once everything
is done, we can do curr = nxt. Wrap that all in a while loop that runs as long as
curr is defined.

Once we reach a point where curr is not defined, we can be finished. This is
because at the end of a linked list, the last node points to undefined. So that
would mean that we are done. 
'''
