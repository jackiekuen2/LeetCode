#  Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        Initilize a dummy linked list l3 with null, and pointer (ptr)
        Algo: 
        i) Check if l1 and l2 exists
        ii) Any l1 or l2 is smaller?
        iii) Add a node to l3, ptr.next = 11.val if l1 is smaller
        iv) mover pointers forward, ptr = ptr.next, l1 = l1.next
        v) iterate...
        """
        # list to return, initialized with 0, pointer is equal to the head
        head = ListNode(0)
        ptr = head

        while True: # Iterate indifinitely, and break out the while-loop if certain condition is met
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                ptr.next = l2 # If l1 is None, add the entire l2
                break
            elif l2 is None:
                ptr.next = l1 # If l1 is None, add the entire l1
                break
            else:
                smallerVal = 0
                if l1.val < l2.val:
                    smallerVal = l1.val
                    l1 = l1.next # move forward the l1 pointer
                else:
                    smallerVal = l2.val
                    l2 = l2.next # move forward the l2 pointer
                
                newNode = ListNode(smallerVal) # This node is not pointing anywhere and nothing is pointing to it
                # The return list is going to have this new node
                ptr.next = newNode
                # move the pointer forward, pointing to new node, with no next value
                ptr = ptr.next

            # returne head's next value
            return head.next