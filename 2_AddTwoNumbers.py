# Repo Only
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# LeetCode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Design:
    # Think of a return buffer for a calculator's display in a full adder.
    # Create a new dummy head node that we will use for the output.
    # Link this node to a node that we will use to progress through the digits.
    # Loop:
    #   Get the each digit from the input list, otherwise have that digit to be 0, so we can progress through the other list or remaining carry.
    #   Add the digits and any previous carry.
    #   Store the 1's digit of the result in a new node and attach it to our linked list.
    #   Calculate the new carry and store it.
    #   Move the pointers for each of our lists if we can.
    #   Keep calculating as long as there is a next value in each input list and we have no carry.
    # Return the list.
    def addTwoNumbers(
        self, 
        l1: Optional[ListNode], 
        l2: Optional[ListNode]
        ) -> Optional[ListNode]:
        # Create a temporary list to put our results in
        tempNode = ListNode(0)

        # Create a variable to track where we are in the list
        tailNode = tempNode

        # Track carry
        carry = 0

        # process as long as we still have a digit
        while l1 is not None or l2 is not None or carry != 0:
            # Grab the value to process, if it exists, otherwise 0
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            # Calculate sum and carry
            sum = digit1 + digit2 + carry
            carry = 1 if (sum > 9) else 0

            # Create the next node with our current digit
            tailNode.next = ListNode(sum % 10)

            # Progress our pointers
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            tailNode = tailNode.next

        # Return next element as the first element is just 0
        return tempNode.next

# Post Analysis:
# Should return the next node of our tempNode, this is our list.