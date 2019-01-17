# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#
#

def listtoint(nums):
    i = 0
    nums = nums[::-1]
    for num in nums:
        i = i*10 + num
    return i


def inttolist(i):
    result_list = []
    while i>0:
        result_list.append(i%10)
        i = int(i/10)
    return result_list

num1 = [2,5,1]
num2 = [4,7,6]
print(inttolist(listtoint(num1) + listtoint(num2)))





