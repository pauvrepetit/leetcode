/*
 * 面试题 02.01. 移除重复节点
 * 
 * 20200920
 * Hu Ao
 */

#include <cstdio>
#include <string>

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
  ListNode *removeDuplicateNodes(ListNode *head) {
    if (head == NULL) {
      return NULL;
    }
    ListNode *hh = head;
    int see[20010];
    memset(see, 0, sizeof(int) * 20010);
    see[head->val] = 1;
    while (head->next != NULL) {
      if (see[head->next->val] == 0) {
        see[head->next->val] = 1;
        head = head->next;
      } else {
        head->next = head->next->next;
      }
    }
    return hh;
  }
};

int main(void) {
  Solution s = Solution();
  ListNode *head = new ListNode(1);
  ListNode *hh = head;
  head->next = new ListNode(2);
  head = head->next;
  head->next = new ListNode(3);
  head = head->next;
  head->next = new ListNode(3);
  head = head->next;
  head->next = new ListNode(2);
  head = head->next;
  head->next = new ListNode(1);
  // head = head->next;
  hh = s.removeDuplicateNodes(hh);
  return 0;
}