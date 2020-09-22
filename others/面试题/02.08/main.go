/*
 * 面试题 02.08. 环路检测
 *
 * 20200922
 * Hu Ao
 *
 * 快慢指针找环，慢指针每次前进1，快指针每次前进2
 * 当二者相遇时，慢指针距离环开始的位置的距离等于链表头到环头的距离
 * 慢指针继续前进，快指针移动到链表头，两个指针速度都变为1，二者再次相遇的位置就是环开始的位置
 */

package main

// ListNode struct
type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	var slow, fast = head, head
	for true {
		slow = slow.Next
		if fast == nil || fast.Next == nil {
			return nil
		}
		fast = fast.Next.Next
		if slow == fast {
			fast = head
			for slow != fast {
				slow = slow.Next
				fast = fast.Next
			}
			return fast
		}
	}
	return nil
}

func main() {

}
