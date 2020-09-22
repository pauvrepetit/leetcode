/*
 * 面试题 02.05. 链表求和
 *
 * 20200922
 * Hu Ao
 */

package main

// ListNode struct
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	l1Back := l1
	for l1.Next != nil && l2.Next != nil {
		sum := l1.Val + l2.Val
		if sum < 10 {
			l1.Val = sum
		} else {
			l1.Val = sum - 10
			l1.Next.Val++
		}
		l1 = l1.Next
		l2 = l2.Next
	}
	l1.Val += l2.Val
	if l1.Next == nil {
		l1.Next = l2.Next
	}
	for l1.Next != nil {
		if l1.Val >= 10 {
			l1.Val -= 10
			l1.Next.Val++
		} else {
			break
		}
		l1 = l1.Next
	}
	if l1.Val >= 10 {
		l1.Val -= 10
		l1.Next = &ListNode{1, nil}
	}
	return l1Back
}
