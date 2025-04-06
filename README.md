# Linked-List-cycle

Linked List Cycle
This repository contains my solution

Problem Description

Given the head of a linked list, determine if the list contains a **cycle**.
A cycle occurs when a node’s `next` pointer points back to a previous node in the list, forming a loop.

example:
Input: head = [3,2,0,-4], pos = 1 Output: True
Explanation: -4 points back to node with value 2, forming a cycle.


Approach

This solution uses **Floyd's Cycle Detection Algorithm** (also known as the **Tortoise and Hare Algorithm**):

- 🐢 `slow` pointer moves one step at a time.
- 🐇 `fast` pointer moves two steps at a time.
- If there is a cycle, both pointers will eventually meet.
