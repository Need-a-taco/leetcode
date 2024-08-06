from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def fst_sol(list1 : Optional[ListNode], list2 : Optional[ListNode]) -> Optional[ListNode]:
    while list1 or list2:
        if list1.val <= list2.val:
            list1.next = list1.next if (list1.next.val <= list2.val) else list2
            list1 = list1.next
        else:
            list2.next = list2.next if (list2.next.val < list1.val) else list1
            list2 = list2.next
    return min(list1, list2)

def neet_sol(list1 : Optional[ListNode], list2 : Optional[ListNode]) -> Optional[ListNode]:
    # These 2 lines est a start of the LL. Common prac... tl will iterate.
    hd = ListNode() 
    tl = hd
    
    # While both are defined
    while (list1 and list2):
        if (list1.val <= list2.val):
            tl.next = list1
            list1 = list1.next
        else:
            tl.next = list2
            list2 = list2.next
        tl = tl.next
    
    # Case 1: list1 is still defined but list2 isn't
    if list1:
        tl.next = list1
    # Case 2: list2 is still defined but list1 isn't 
    elif list2:
        tl.next = list2
    return hd.next
'''
Notes...
Solution: Here, we are learning a common practice in linked list problems. Establish a dummy
variable that we never refer to. We just use it so that we have something to build off of. In 
this implementation, we call this the head. Since we don't know the length of the output, we
will just have the tail iterate and get further from the head one node at a time. 
'''
#############################################################################################
# Testing

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3
            
neet_sol(a1, b1)
current_node = a1
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next