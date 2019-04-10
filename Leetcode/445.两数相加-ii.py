#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (46.24%)
# Total Accepted:    2.7K
# Total Submissions: 5.7K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
# 
# 
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 进阶:
# 
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 
# 示例:
# 
# 
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        carry = 0
        a = l1
        b = l2

        while a.next is not None and b.next is not None
            len_a = len_b = 1
            while a.next is not None:
                len_a += 1
                a = a.next
            while b.next is not None:
                len_b += 1
                b = b.next

            cur.val = (a.val + b.val + carry) % 10
            carry = (a.val + b.val + carry) // 10


            new = ListNode(0)
            new.next = cur
            for i in range(len_a):
                a = a.next
            a = None
            b = None
            

