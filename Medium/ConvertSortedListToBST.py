# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Idea: a sorted list is just the inorder traversal of a BST
#This one was pretty easy, just gotta get the sorted List
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        sortedList = [] #O(n) space
        while head: #O(n) time, convert to sorted list
            sortedList.append(head.val)
            head = head.next
        
        return self.constructBalancedBST(sortedList)
    
    def constructBalancedBST(self,L):
        if not L: return None #Remember the base-case
        median = len(L)//2
        root = TreeNode(L[median])
        root.left = self.constructBalancedBST(L[:median])
        root.right = self.constructBalancedBST(L[median+1:])
        
        return root