/*
 * 面试题 02.07. 链表相交
 *
 * 20200922
 * Hu Ao
 */

package main

import (
	"fmt"
)

// ListNode struct
type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	var ha = headA
	var hb = headB
	var countA, countB int
	for ; ha != nil; ha = ha.Next {
		countA++
	}
	for ; hb != nil; hb = hb.Next {
		countB++
	}
	if countA < countB {
		headA, headB = headB, headA
		countA, countB = countB, countA
	}
	for i := 0; i < (countA - countB); i++ {
		headA = headA.Next
	}
	return sol(headA, headB)
}

func sol(headA, headB *ListNode) *ListNode {
	for headA != headB {
		headA = headA.Next
		headB = headB.Next
	}
	return headA
	// if headA == headB {
	// 	return headA
	// }
	// return sol(headA.Next, headB.Next)
}

func main() {
	var headA = &ListNode{4, &ListNode{1, &ListNode{8, &ListNode{4, &ListNode{5, nil}}}}}
	var headB = &ListNode{5, &ListNode{0, &ListNode{1, headA.Next.Next}}}
	var commonNode = getIntersectionNode(headA, headB)
	fmt.Println(commonNode.Val)
}
