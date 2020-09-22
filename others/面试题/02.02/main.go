/*
 * 面试题 02.02. 返回倒数第 k 个节点
 *
 * 20200922
 * Hu Ao
 */

package main

import "fmt"

// ListNode struct
type ListNode struct {
	Val  int
	Next *ListNode
}

func kthToLast(head *ListNode, k int) int {
	knode := head
	for i := 0; i < k; i++ {
		head = head.Next
	}
	for head != nil {
		knode = knode.Next
		head = head.Next
	}
	return knode.Val
}

func main() {
	head := &ListNode{1, nil}
	h := head
	head.Next = &ListNode{2, nil}
	head = head.Next
	head.Next = &ListNode{3, nil}
	head = head.Next
	head.Next = &ListNode{4, nil}
	head = head.Next
	head.Next = &ListNode{5, nil}

	fmt.Println(kthToLast(h, 2))
}
