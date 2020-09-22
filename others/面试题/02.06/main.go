/*
 * 面试题 02.06. 回文链表
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

func isPalindrome(head *ListNode) bool {
	var numList []int
	for head != nil {
		numList = append(numList, head.Val)
		head = head.Next
	}
	numCount := len(numList)
	for i := 0; i < numCount/2; i++ {
		if numList[i] != numList[numCount-i-1] {
			return false
		}
	}
	return true
}

func main() {

}
