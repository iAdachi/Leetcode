# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val= 0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        root = ListNode()
        currentNode = root
        carry = 0
        while l1 or l2 or carry != 0:
            if l1: v1 = l1.val # if exist l1 and l2
            else: v1 = 0

            if l2: v2 = l2.val
            else: v2 = 0
            
            currentNode.next = ListNode() 
            currentNode = currentNode.next

            currentNode.val = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10

            if l1: l1 = l1.next
            else: l1 = None
            if l2: l2 = l2.next
            else: l2 = None
        '''       
        if carry != 0: 
            currentNode.next = ListNode()
            currentNode = currentNode.next
            currentNode.val = carry
        '''  
        return root.next

# Aditional functions for using the solution
def createLinkedList(l):
    """
    :type l: List[int]
    :rtype: [ListNode]
    """

    root = ListNode()
    currentElement = root

    for i, j in enumerate(l):
        currentElement.val = j
        if i < len(l) - 1: 
            currentElement.next = ListNode()
            currentElement = currentElement.next
    return root

def printList(root):
    """
    :type l: [ListNode]
    """
    currentNode = root
    while True:
        print(currentNode.val)
        if currentNode.next == None: break
        currentNode = currentNode.next

# Example 
a = [9,9,9,9,9,9,9]
b = [9,9,9,9]

# Create the linked list
r1 = createLinkedList(a)
r2 = createLinkedList(b)

# Add 
mySol = Solution()
result = mySol.addTwoNumbers(r1, r2)



