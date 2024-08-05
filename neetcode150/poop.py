
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

current_node = node1
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next
